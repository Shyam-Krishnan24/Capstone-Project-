
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
df = pd.read_csv("../data/music_listeners.csv")

# Select features
features = [
    "listening_hours_per_week",
    "songs_per_day",
    "skip_rate",
    "playlist_count"
]

X = df[features]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Train model
kmeans.fit(X_scaled)

# Save model and scaler
joblib.dump(kmeans, "model.pkl")
joblib.dump(scaler, "scaler.pkl")

# Display cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)

centers_df = pd.DataFrame(
    cluster_centers,
    columns=features
)

print("\nCluster Centers:")
print(centers_df)

print("\nCluster Distribution:")
print(pd.Series(kmeans.labels_).value_counts().sort_index())

print("\nModel and scaler saved successfully.")

