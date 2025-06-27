# 🌦️ Cloud-Based Weather Tracker Web App (GCP + Firebase)

A smart, cloud-native weather tracking system that:
- 🪣 Accepts weather data via **Google Cloud Storage**
- ☁️ Uses **Cloud Functions** to process the data
- 📩 Publishes updates to **Firestore Database**
- 🖥️ Displays real-time data via a **Firebase + HTML/JS dashboard**

---

## 🧩 Tech Stack / Cloud Services Used

| Service                      | Purpose                                               |
|-----------------------------|-------------------------------------------------------|
| **Google Cloud Storage (GCS)** | Upload JSON weather files (input trigger)              |
| **Cloud Pub/Sub**              | (Behind the scenes via Eventarc) - connects GCS to Cloud Function |
| **Cloud Functions (Gen 2)**    | Parses JSON files & updates Firestore                 |
| **Firestore (Firebase DB)**    | Stores real-time weather data                        |
| **Firebase Hosting (optional)**| Hosts the dashboard webpage (or run locally)         |
| **HTML + JavaScript (Frontend)** | Displays weather in a real-time table format          |

---

## 🧠 How It Works

1. **User uploads a `.json` file** (e.g., `pune.json`) to a GCS bucket.
2. This triggers a **Cloud Function**, which:
   - Reads the file
   - Extracts fields like `City`, `Temperature`, `Humidity`, `Condition`
   - Writes them to **Firestore**
3. The **dashboard web app** listens to Firestore updates using `onSnapshot()`
4. You instantly see updated rows on the **weather dashboard** — no refresh needed!

---

## 📂 Sample JSON Input (uploaded to bucket)

```json
{
  "City": "Pune",
  "Temperature": 32,
  "Humidity": 45,
  "Condition": "Sunny"
}

weather-function/
├── main.py                 # Cloud Function source
├── requirements.txt        # Python dependencies
dashboard/
└── index.html              # Real-time frontend UI

✅ Steps to Deploy (Summarized)
1.Create GCP Project
2.Enable Cloud Functions, GCS, Pub/Sub, Firestore
3.Create GCS Bucket and Pub/Sub topic
4.Write and deploy Cloud Function
5.Enable Firestore in Firebase
6.Upload .json files to GCS



