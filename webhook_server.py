import os
from flask import Flask, request
import requests

app = Flask(name)

TELEGRAM_BOT_TOKEN = "8970384040:AAGPz9UKpVj7A2z9Gmc___GqmR848bc5Z40"
TELEGRAM_CHAT_ID = "-100430144920"

def send_telegram(message):
    url = "https://api.telegram.org/bot" + TELEGRAM_BOT_TOKEN + "/sendMessage"
    payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", "Alert triggered!")
    send_telegram("TradingView Alert: " + message)
    return "OK", 200

if name == "main":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
