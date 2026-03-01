from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
from db import forecast_collection
from scheduler import send_daily_email

app = Flask(__name__)



@app.route("/set-email", methods=["POST"])
def set_email():

    data = request.json
    recipient = data.get("email")

    if not recipient:
        return jsonify({"error": "Email required"}), 400

    forecast_collection.insert_one({
        "type": "email_config",
        "recipient": recipient
    })

    return jsonify({"message": "Recipient email set successfully"})




@app.route("/generate-forecast", methods=["GET"])
def generate_now():

    try:
        send_daily_email()
        return jsonify({"message": "Forecast generated & email sent"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500




@app.route("/")
def home():
    return jsonify({"status": "Weather API Running"})



scheduler = BackgroundScheduler()
scheduler.add_job(send_daily_email, "cron", hour=13, minute=45)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run(debug=True)