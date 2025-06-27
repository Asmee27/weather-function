import functions_framework
import json
from google.cloud import firestore

@functions_framework.cloud_event
def fetch_weather(cloud_event):
    import base64
    import os

    # File info from GCS
    bucket = cloud_event.data["bucket"]
    name = cloud_event.data["name"]

    # Download file from GCS
    from google.cloud import storage
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket)
    blob = bucket.blob(name)
    content = blob.download_as_text()

    # Parse JSON
    weather_data = json.loads(content)

    # Upload to Firestore
    db = firestore.Client()
    for item in weather_data:
        db.collection("weather").add(item)

    print("Weather data uploaded to Firestore successfully.")
