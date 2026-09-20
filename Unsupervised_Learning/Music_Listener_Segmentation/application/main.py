from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field


BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_DIR = BASE_DIR / "ml model" / "models"
MODEL_PATH = MODEL_DIR / "model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
CLUSTER_NAMES_PATH = MODEL_DIR / "cluster_names.pkl"
FEATURE_COLUMNS = [
    "listening_hours_per_week",
    "songs_per_day",
    "skip_rate",
    "playlist_count",
]

try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    cluster_names = joblib.load(CLUSTER_NAMES_PATH)
except Exception as exc:
    raise RuntimeError(
        f"Unable to load segmentation artifacts from {MODEL_DIR}: {exc}"
    ) from exc


class ListenerInput(BaseModel):
    listening_hours_per_week: float = Field(ge=2, le=38)
    songs_per_day: float = Field(ge=10, le=145)
    skip_rate: float = Field(ge=3, le=65)
    playlist_count: float = Field(ge=2, le=40)


class SegmentationResponse(BaseModel):
    cluster_id: int
    segment: str


app = FastAPI(
    title="Music Listener Segmentation API",
    description="Assigns listeners to a meaningful K-Means segment.",
    version="1.0.0",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8501", "http://127.0.0.1:8501"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home() -> dict[str, str]:
    return {"message": "Music Listener Segmentation API is running"}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}


@app.post("/predict", response_model=SegmentationResponse)
def predict(listener: ListenerInput) -> SegmentationResponse:
    input_data = pd.DataFrame([listener.model_dump()])[FEATURE_COLUMNS]
    scaled_input = scaler.transform(input_data)
    cluster_id = int(model.predict(scaled_input)[0])

    segment = cluster_names.get(cluster_id, cluster_names.get(str(cluster_id)))
    if segment is None:
        raise HTTPException(
            status_code=500,
            detail=f"No segment name is configured for cluster {cluster_id}.",
        )

    return SegmentationResponse(cluster_id=cluster_id, segment=segment)
