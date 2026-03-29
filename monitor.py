import psutil
import time
import os

THRESHOLD = 75

while True:
    cpu = psutil.cpu_percent(interval=2)
    print(f"CPU Usage: {cpu}%")

    if cpu > THRESHOLD:
        print("Threshold exceeded. Triggering scale...")

        os.system("gcloud compute instances start auto-scale-vm --zone=us-central1-a")
        os.system("gcloud compute ssh auto-scale-vm --zone=us-central1-a --command=\"nohup python3 app.py &\"")

        break

    time.sleep(5)
