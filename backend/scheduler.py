from datetime import datetime
from db import forecast_collection
from forecast import generate_forecast
from email_utils import send_email

def send_daily_email():

    forecast_data = generate_forecast()

    today = datetime.now().strftime("%Y-%m-%d")

    # Store forecast in MongoDB
    forecast_collection.insert_one({
        "date_generated": today,
        "forecast": forecast_data
    })

    # Get recipient from DB (latest configured email)
    config = forecast_collection.find_one(
        {"type": "email_config"},
        sort=[("_id", -1)]
    )

    if config and "recipient" in config:
        send_email(config["recipient"], forecast_data)