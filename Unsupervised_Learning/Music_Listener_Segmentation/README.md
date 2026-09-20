# Music Listener Segmentation

This project groups listeners into meaningful segments using a trained K-Means model.

## Segments

- **Casual Listener**: lower activity, fewer songs and playlists, higher skip rate
- **Music Explorer**: moderate activity across the listener features
- **Heavy Listener**: highest activity, most playlists, and lowest skip rate

## Project Layout

```text
Music_Listener_Segmentation/
├── analysis/                  # Exploratory notebook
├── data/                      # Source dataset
├── graphs/                    # Generated visualizations
├── ml model/
│   ├── train_model.ipynb      # Training and evaluation notebook
│   └── models/                # Saved model artifacts and metrics
├── application/
│   ├── app.py                 # Streamlit frontend
│   └── main.py                # FastAPI backend
├── requirements.txt
└── README.md
```

## Setup

From this directory, create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

The application loads these existing artifacts from `ml model/models/`:

- `model.pkl`
- `scaler.pkl`
- `cluster_names.pkl`

To retrain the model, run all cells in `ml model/train_model.ipynb` from the `ml model` directory.

## Run the Backend

Open a terminal in this directory and run:

```powershell
uvicorn application.main:app --reload --port 8000
```

The API is available at `http://127.0.0.1:8000`. Interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## API

### `GET /health`

Returns the backend health status.

### `POST /predict`

Request body:

```json
{
  "listening_hours_per_week": 6,
  "songs_per_day": 24,
  "skip_rate": 45,
  "playlist_count": 5
}
```

Response:

```json
{
  "cluster_id": 2,
  "segment": "Casual Listener"
}
```

The accepted input ranges match the values used to train the model:

| Feature | Minimum | Maximum |
|---|---:|---:|
| listening_hours_per_week | 2 | 38 |
| songs_per_day | 10 | 145 |
| skip_rate | 3 | 65 |
| playlist_count | 2 | 40 |

## Run the Frontend

Keep the backend running, open another terminal in this directory, and run:

```powershell
streamlit run application/app.py
```

Open the displayed Streamlit URL, enter the four listener values, and select **Find listener segment**. The frontend sends the input to FastAPI and displays the named segment returned by the model.

To use a different backend URL:

```powershell
$env:SEGMENTATION_API_URL = "http://127.0.0.1:8000"
streamlit run app.py
```

### TO get values in running

4, 19, 50, 4 → Casual Listener
14, 58, 25, 16 → Music Explorer
30, 121, 8, 29 → Heavy Listener