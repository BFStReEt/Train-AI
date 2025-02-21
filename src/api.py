from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API xử lý chat"}

@app.get("/download-excel/")
def download_excel():
    return {"file": "output.xlsx"}

# Chạy API bằng lệnh: uvicorn src.api:app --reload
