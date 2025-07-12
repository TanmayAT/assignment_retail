from fastapi import FastAPI, HTTPException, Request
import joblib
import pandas as pd
import redis
import json
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
import logging
import os

redis_host = os.getenv("REDIS_HOST", "redis-service")
redis_port = int(os.getenv("REDIS_PORT", "6379"))

redis_client = redis.Redis(host=redis_host, port=redis_port, db=0)

app = FastAPI()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='/app/app.log'
)
logger = logging.getLogger(__name__)

logger.info("Starting Retail Model API")
logger.info(f"Connecting to Redis at {redis_host}:{redis_port}")

# Middleware for CORS
middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
]

# Load models once at startup
try:
    faster_pipeline = joblib.load("faster_closing_model.pkl")
    return_pipeline = joblib.load("high_return_model.pkl")
    logger.info("Models loaded successfully")
except Exception as e:
    logger.error(f"Error loading models: {str(e)}")
    raise RuntimeError("Model loading failed")

@app.middleware("http")
async def middleware(request: Request, call_next):
    try:
        response = await call_next(request)
        logger.info(f"Request: {request.method} {request.url}")
        logger.info(f"Response status: {response.status_code}")
        return response
    except Exception as e:
        logger.error(f"Middleware error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/")
async def root():
    return {"message": "Welcome to the Retail Model API. Use /predict/ endpoint to get predictions."}

@app.post("/predict/")
async def predict(request: Request):
    try:
        input_data = await request.json()
        input_str = json.dumps(input_data)
        logger.debug(f"Received input data: {input_data}")

        # Check cache (optional)
        cached_result = redis_client.get(input_str)
        if cached_result:
            logger.info("Returning cached result")
            return json.loads(cached_result)

        # Predict
        input_df = pd.DataFrame([input_data])
        logger.debug(f"Input DataFrame: {input_df}")

        faster = faster_pipeline.predict(input_df)
        high_return = return_pipeline.predict(input_df)

        result = {
            "faster_closing_score": round(float(faster[0]), 2),
            "high_return_score": round(float(high_return[0]), 2)
        }

        # Cache result
        redis_client.set(input_str, json.dumps(result))
        logger.info(f"Prediction result: {result}")

        return result

    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed: " + str(e))
