import csv
import os
from datetime import datetime

FILE_NAME = "monitor_log.csv"

def log_result(url, status, latency, error=""):
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, mode="a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "timestamp",
                "url",
                "status",
                "latency_seconds",
                "error"
            ])

        writer.writerow([
            datetime.now().isoformat(),
            url,
            status,
            latency,
            error
        ])
