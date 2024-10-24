from fastapi import FastAPI
import time
import csv
from asyncio import sleep

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

@app.get("/file_read")
def file_read():
    with open('../data/tested.csv', 'r') as file:
        csv_reader = csv.reader(file)
        last_row = None
        for row in csv_reader:
            pass
    return {"message": "file_read"}

@app.get("/wait_time")
async def wait_time():
    await sleep(1)
    return {"message": "time_sleep"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
