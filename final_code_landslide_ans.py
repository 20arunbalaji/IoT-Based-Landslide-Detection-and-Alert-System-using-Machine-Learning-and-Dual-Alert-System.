from flask import Flask, render_template
import RPi.GPIO as GPIO
import adafruit_dht
import joblib
import numpy as np
import time
import board
import threading
import requests  # For Telegram

app = Flask(__name__)

# Load the trained ML model
model = joblib.load("/home/arun/Desktop/ Landslide/landslide ML_model.pkl")  # Ensure correct path

# Sensor value sets (Two "No Risk" + One "High Risk")
sensor_data_sets = [
    {"soil_moisture": 42.5, "vibration": 3.2, "temperature": 32.5},  # No risk
    {"soil_moisture": 39.8, "vibration": 0, "temperature": 32.7},  # No risk
    {"soil_moisture": 85.0, "vibration": 7.5, "temperature": 35.2},  # High risk
]

current_sensor_values = sensor_data_sets[0]
last_prediction = None  # To avoid repeated alerts

# === Telegram Bot Setup ===
BOT_TOKEN = "8177265213:AAGs5OltKgi6xCZg_ZKf3OfCyyuNCcWNFXg"
CHAT_ID = "-1002656452215"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=data)

def update_sensor_data():
    """Loop through sensor data sets every 2 seconds."""
    global current_sensor_values
    index = 0
    while True:
        current_sensor_values = sensor_data_sets[index]
        index = (index + 1) % len(sensor_data_sets)
        time.sleep(2)

def check_and_alert():
    """Check for high-risk predictions and send alerts once per change."""
    global last_prediction
    while True:
        data = get_sensor_data()
        prediction_text = data['prediction']
        
        # Only send message if it's a new "high risk" prediction
        if prediction_text != last_prediction:
            last_prediction = prediction_text
            if "Warning: High chance of landslide" in prediction_text:
                message = (
                    f"🌍 *Landslide Alert System*\n"
                    f"🟫 Soil Moisture: {data['soil_moisture']}\n"
                    f"🌀 Vibration: {data['vibration']}\n"
                    f"🌡️ Temperature: {data['temperature']}\n"
                    f"📢 *Prediction:* {prediction_text}"
                )
                send_telegram_message(message)
        time.sleep(2)

def get_sensor_data():
    """Fetch current sensor values and predict landslide risk."""
    soil_moisture = current_sensor_values["soil_moisture"]
    vibration = current_sensor_values["vibration"]
    temperature = current_sensor_values["temperature"]

    input_data = np.array([[soil_moisture, vibration, temperature]])
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        result = "⚠️ Warning: High chance of landslide!"
    else:
        result = "✅ No landslide risk detected."

    return {
        "soil_moisture": f"{soil_moisture:.1f}%",
        "vibration": f"{vibration:.1f}",
        "temperature": f"{temperature:.1f}°C",
        "prediction": result
    }

@app.route("/")
def home():
    data = get_sensor_data()
    return f"""
    <h1>Landslide Prediction System</h1>
    <p><b>Soil Moisture:</b> {data['soil_moisture']}</p>
    <p><b>Vibration:</b> {data['vibration']}</p>
    <p><b>Temperature:</b> {data['temperature']}</p>
    <h2>Prediction: {data['prediction']}</h2>
    """

if __name__ == "__main__":
    # Start threads
    threading.Thread(target=update_sensor_data, daemon=True).start()
    threading.Thread(target=check_and_alert, daemon=True).start()

    # Run the web app
    app.run(host="0.0.0.0", port=5000, debug=True)
