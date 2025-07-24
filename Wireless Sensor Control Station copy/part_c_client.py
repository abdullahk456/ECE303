import requests
import time

url = "http://172.20.10.7"  # ✅ Arduino’s IP

payload = {
    "red": 128,
    "blue": 1
}

while True:
    try:
        response = requests.post(url, json=payload, timeout=5)
        print(f"📤 Sent data: {payload}")
        print(f"📥 Response: {response.text}")
    except Exception as e:
        print("❌ Error:", e)

    time.sleep(10)
