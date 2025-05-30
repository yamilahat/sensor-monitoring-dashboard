import requests, random, time
from datetime import datetime

url = "http://fastapi-backend:8000/api/readings"

sensors = ["temp-01", "humidity-01", "co2-01"]

while True:
  data = {
    "sensor_id": random.choice(sensors),
    "value": round(random.uniform(20.0, 30.0), 2),
    "timestamp": datetime.utcnow().isoformat()
  }

  try:
    res = requests.post(url, json=data)
    print(f"Sent: {data} | Status: {res.status_code}")

  except requests.exceptions.RequestException as e:
    print(f"[ERROR] Failed to send data: {e}")

  time.sleep(5)
