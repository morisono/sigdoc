import gspread
import pandas as pd

# Authenticate with Google and get the sheet
URL = 'https://docs.google.com/spreadsheets/d/1_91Vps76SKOdDQ8cFxZQdgjTJiz23375sAT7vPvaj4k/edit#gid=0'

gc = gspread.service_account("path/to/key.json")
sh = gc.open_by_url(URL)
worksheet = sh.sheet1

def get_data():
    values = worksheet.get_all_values()
    df = pd.DataFrame(values[1:], columns=values[0])
    return df

with gr.Blocks() as demo:
    gr.Markdown("# 📈 Real-Time Line Plot")
    with gr.Row():
        with gr.Column():
            gr.DataFrame(get_data, every=5)
        with gr.Column():
            gr.LinePlot(get_data, every=5, x="Date", y="Sales", y_title="Sales ($ millions)", overlay_point=True, width=500, height=500)

demo.queue().launch()  # Run the demo with queuing enabled
demo.queue().launch()  # Run the demo with queuing enabled