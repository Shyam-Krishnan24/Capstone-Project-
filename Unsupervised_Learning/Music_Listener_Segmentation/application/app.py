import os

import requests
import streamlit as st


st.set_page_config(
    page_title="Music Listener Segmentation",
    page_icon="🎵",
    layout="centered",
)

API_URL = os.getenv("SEGMENTATION_API_URL", "http://127.0.0.1:8000")

st.title("Music Listener Segmentation")
st.write("Enter listener behavior to identify the closest listener segment.")

with st.form("listener_form"):
    listening_hours = st.number_input(
        "Listening hours per week",
        min_value=2.0,
        max_value=38.0,
        value=15.0,
        step=0.5,
    )
    songs_per_day = st.number_input(
        "Songs per day",
        min_value=10.0,
        max_value=145.0,
        value=60.0,
        step=1.0,
    )
    skip_rate = st.number_input(
        "Skip rate",
        min_value=3.0,
        max_value=65.0,
        value=29.0,
        step=1.0,
    )
    playlist_count = st.number_input(
        "Playlist count",
        min_value=2.0,
        max_value=40.0,
        value=15.0,
        step=1.0,
    )
    submitted = st.form_submit_button("Find listener segment", type="primary")

if submitted:
    payload = {
        "listening_hours_per_week": listening_hours,
        "songs_per_day": songs_per_day,
        "skip_rate": skip_rate,
        "playlist_count": playlist_count,
    }

    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        response.raise_for_status()
        result = response.json()
        st.success(result["segment"])
        st.caption(f"Cluster ID: {result['cluster_id']}")
    except requests.exceptions.ConnectionError:
        st.error("The backend is unavailable. Start FastAPI before making a prediction.")
    except requests.exceptions.Timeout:
        st.error("The backend took too long to respond. Try again.")
    except requests.exceptions.HTTPError as exc:
        detail = response.text if response is not None else str(exc)
        st.error(f"The backend rejected the input: {detail}")
    except (KeyError, ValueError) as exc:
        st.error(f"The backend returned an unexpected response: {exc}")
