import requests
import time
from datetime import datetime
from logger import log_result

URLS = [
    "https://google.com",
    "https://example.com"
]

CHECK_INTERVAL = 60  # seconds

def check_site(url):
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        latency = round(time.time() - start, 2)

        status = response.status_code

        if status == 200:
            print(f"[{datetime.now()}] ✅ {url} UP | {latency}s")
            log_result(url, "UP", latency)
        else:
            print(f"[{datetime.now()}] ⚠️ {url} DOWN | Status: {status}")
            log_result(url, "DOWN", latency, f"Status {status}")

    except Exception as e:
        print(f"[{datetime.now()}] ❌ {url} ERROR | {e}")
        log_result(url, "ERROR", "", str(e))


if __name__ == "__main__":
    print("🚀 Website Monitor Started...\n")

    while True:
        for site in URLS:
            check_site(site)

        print("-" * 50)
        time.sleep(CHECK_INTERVAL)
