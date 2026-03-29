# 🚀 Auto-Scaling Local VM to Cloud (GCP)

## 📌 Overview
This project demonstrates a hybrid cloud setup where a **local virtual machine monitors its CPU usage** and automatically **triggers a cloud VM (Google Cloud Platform)** when usage exceeds a defined threshold (75%). A sample application is then deployed on the cloud VM and made accessible via a web browser.

---

## 🎯 Objective
- Monitor resource usage (CPU) on a local VM  
- Automatically trigger scaling to cloud when threshold exceeds  
- Deploy and run an application on the cloud VM  
- Demonstrate end-to-end automation  

---

## 🧠 Architecture

```mermaid
flowchart TD

A[Local Machine Terminal] --> B[Local VM (VirtualBox)]

B --> C[monitor.py (psutil)]
C -->|CPU < 75%| C
C -->|CPU > 75%| D[gcloud CLI Trigger]

D --> E[GCP Compute Engine VM]

E --> F[app.py Deployment]
F --> G[HTTP Server Running :8080]

G --> H[User Browser Access]
