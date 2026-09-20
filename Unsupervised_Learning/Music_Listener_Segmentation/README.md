# Music Listener Segmentation

This project groups listeners into three segments using a trained K-Means model:

- **Casual Listener**: lower activity and higher skip rate
- **Music Explorer**: moderate listening activity
- **Heavy Listener**: highest activity and lowest skip rate

## Setup

Open PowerShell in the `Music_Listener_Segmentation` directory:

```powershell
cd "Unsupervised_Learning\Music_Listener_Segmentation"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

If the virtual environment already exists, only activate it and continue.
The application uses the saved files in `ml model/models/`.

## Input Ranges

| Input | Minimum | Maximum |
|---|---:|---:|
| Listening hours per week | 2 | 38 |
| Songs per day | 10 | 145 |
| Skip rate | 3 | 65 |
| Playlist count | 2 | 40 |

## Run the Backend

Open Terminal 1 and run:

```powershell
cd "Unsupervised_Learning\Music_Listener_Segmentation"
.\.venv\Scripts\Activate.ps1
python -m uvicorn application.main:app --reload --port 8002
```

The backend runs at `http://127.0.0.1:8002`.

## Run the Frontend

Keep the backend running. Open Terminal 2 and run:

```powershell
cd "Unsupervised_Learning\Music_Listener_Segmentation"
.\.venv\Scripts\Activate.ps1
streamlit run application/app.py --server.port 8502
```

Open `http://localhost:8502` in a browser.

## Test Values

Enter the following values into the four frontend fields.

| Test | Listening hours | Songs per day | Skip rate | Playlist count | Expected segment |
|---|---:|---:|---:|---:|---|
| Casual listener | 4 | 19 | 50 | 4 | Casual Listener |
| Music explorer | 14 | 58 | 25 | 16 | Music Explorer |
| Heavy listener | 30 | 121 | 8 | 29 | Heavy Listener |

Select **Find listener segment** after entering each row. The frontend should
display the segment name and cluster ID.

## Stop the Project

Press `Ctrl+C` in both terminals when testing is complete.