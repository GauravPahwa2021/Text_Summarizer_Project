import os
import sys
import uvicorn
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from src.textSummarizer.pipeline.prediction_pipeline import PredictionPipeline

text:str

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def training():
    try:
        os.system("Python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")
    

@app.post("/predict")
async def predict_route(text):
    try:
        obj = PredictionPipeline()
        output = obj.predict(text)
        return output
    except Exception as e:
        raise e
    
if __name__ == "__main__":
    uvicorn.run(app,host="0.0.0.0",port=8080)