# Intelligent IoT-based Landslide Prediction and Notification System Using Machine Learning and Chatbot

## 👨‍💻 Author
- Arunbalaji M (21BEC2141)  
- **Project Guide**: Dr. Sujatha Rajkumar (Professor Grade 1)

---

## 🧠 Overview

This project presents an intelligent landslide early warning system that combines **real-time IoT sensing**, **machine learning**, and **dual alert mechanisms** (Telegram bot + Flask web app). It is designed to help **remote or mountainous areas** by detecting early signs of landslides and notifying communities or authorities instantly.

---

## 🎯 Objectives

- Predict landslides using **Random Forest Classifier** based on sensor data.
- Alert users via **Telegram** and **Flask web dashboard**.
- Ensure the system is **low-cost**, **scalable**, and deployable in areas with limited infrastructure.

---

## 🧩 Features

- 📊 **Real-time monitoring** of temperature, soil moisture, and vibration.
- 🤖 Machine Learning-based **risk classification**.
- 📱 **Telegram Bot** for instant mobile notifications.
- 🌐 **Flask Web App** for live data visualization.
- ⚡ Modular & lightweight system architecture for field deployment.

---

## 🛠️ Hardware Used

- Raspberry Pi 5  
- DHT22 Temperature & Humidity Sensor  
- Soil Moisture Sensor (YL-83)  
- Vibration Sensor (SW-420)  
- Power Supply, Wires, Breadboard, Case, etc.

---

## 💻 Software Stack

- **Python 3**  
- **Libraries**: `scikit-learn`, `flask`, `joblib`, `requests`, `numpy`, `RPi.GPIO`, `adafruit_dht`  
- **Machine Learning**: `RandomForestClassifier`  
- **Communication**: Telegram Bot API  
- **Dashboard**: Flask Web Framework

---

## ⚙️ System Workflow

1. **Data Collection**: Sensor data from GPIO pins.
2. **Prediction**: Trained Random Forest model classifies risk level.
3. **Notification**:
   - Sends warning via **Telegram Bot**.
   - Updates live dashboard via **Flask**.
4. **Threading**: Ensures parallel running of alerting and server processes.

---

## 📷 Output Snapshots

- Soil moisture detection & response
- Vibration spike warning
- Telegram alert messages
- Flask live web display with real-time values

---

## 🚫 Limitations

- Internet required for Telegram alerts.
- Limited sensor variety (no rainfall or tilt sensor yet).
- Model trained on small-scale data.
- Power backup (solar/battery) not integrated.

---

## 🚀 Future Enhancements

- Add **rainfall**, **barometric**, and **tilt sensors**.
- Integrate **GPS tagging** and **cloud dashboard**.
- Use **solar power** for off-grid deployment.
- Enhance ML model using LSTM or CNN.
- Add **mobile app** support for wider accessibility.
- Collaborate with disaster response agencies via API.

---

## 🌍 Social & Environmental Impact

- Early alerts can save lives during **sudden landslides**.
- Low-cost design helps **rural/remote communities**.
- Supports **climate resilience** and **SDG-11** goals.
- Reduces manual survey risk and environmental degradation.

---

## 📅 Timeline Summary

| Phase | Duration | Tasks |
|-------|----------|-------|
| Setup & Design | Dec 20 – Jan 10 | Sensor wiring, RPi config |
| Data & ML | Jan 11 – Jan 31 | Dataset creation, model training |
| Alert Systems | Feb 1 – Feb 10 | Flask & Telegram integration |
| Testing & Debugging | Feb 11 – Mar 15 | Real-time validation |
| Finalization | Mar 16 – Apr 14 | Documentation & Submission |

---
