from fastapi import FastAPI, Request, Form
from fastapi.responses import JSONResponse
import gradio as gr
import uvicorn
import logging
import sys
import polars as pl
import threading

app = FastAPI(title="Test API")

# Logger setup
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter(
    "%(asctime)s [%(processName)s: %(process)d] [%(threadName)s: %(thread)d] [%(levelname)s] %(name)s: %(message)s"
)
stream_handler.setFormatter(log_formatter)
logger.addHandler(stream_handler)

logger.info('API is starting up')

# Initialize empty DataFrame for logs
df_logs = pl.DataFrame({
    "time": [],
    "ip": [],
    "method": [],
    "user_agent": [],
    "cookies": [],
    "endpoint": []
})

@app.middleware("http")
async def log_requests(request: Request, call_next):
    global df_logs
    logger.info('Request received')
    
    response = await call_next(request)

    # Collect log data
    log_data = {
        "time": [str(request.headers.get("date", ""))],
        "ip": [request.client.host],
        "method": [request.method],
        "user_agent": [str(request.headers.get("user-agent", ""))],
        "cookies": [str(request.cookies)],
        "endpoint": [str(request.url)]
    }
    
    # Append new log data to the DataFrame
    df_logs = df_logs.vstack(pl.DataFrame(log_data))
    
    return response

@app.post('/push')
async def push():
    global df_logs
    logger.info('POST /push')
    
    # Collect log data
    log_data = {
        "time": [""],
        "ip": ["N/A"],
        "method": ["POST"],
        "user_agent": ["N/A"],
        "cookies": ["N/A"],
        "endpoint": ["Test Button"]
    }
    
    # Append new log data to the DataFrame
    df_logs = df_logs.vstack(pl.DataFrame(log_data))
    
    return JSONResponse(content={"message": "Button pushed and logged!"})

@app.post('/submit_form')
async def submit_form(name: str = Form(...), email: str = Form(...)):
    global df_logs
    logger.info('POST /submit_form')
    
    # Collect log data
    log_data = {
        "time": [""],
        "ip": ["N/A"],
        "method": ["POST"],
        "user_agent": ["N/A"],
        "cookies": ["N/A"],
        "endpoint": [f"Form submitted: {name}, {email}"]
    }
    
    # Append new log data to the DataFrame
    df_logs = df_logs.vstack(pl.DataFrame(log_data))
    
    return JSONResponse(content={"message": "Form submitted and logged!"})

@app.get('/')
async def main():
    logger.info('GET /')
    return 'ok'

@app.get("/logs")
async def get_logs():
    return df_logs.to_dict()

def run_app():
    uvicorn.run(app, host="0.0.0.0", port=5000)

def push_button():
    try:
        response = requests.post("http://localhost:5000/push")
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def submit_form(name, email):
    try:
        response = requests.post("http://localhost:5000/submit_form", data={"name": name, "email": email})
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

with gr.Blocks() as demo:
    with gr.Row():
        gr.Markdown("## API Logs")
        log_df = gr.DataFrame(df_logs)
    with gr.Row():
        push_btn = gr.Button("Push Button")
        push_btn.click(push_button, outputs=log_df)
    with gr.Row():
        name_input = gr.Textbox(label="Name")
        email_input = gr.Textbox(label="Email")
        submit_btn = gr.Button("Submit Form")
        submit_btn.click(submit_form, inputs=[name_input, email_input], outputs=log_df)

if __name__ == "__main__":
    threading.Thread(target=run_app).start()
    demo.launch(share=True, inbrowser=True)
