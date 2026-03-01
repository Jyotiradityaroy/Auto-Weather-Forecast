import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

def send_email(recipient, forecast_data):

    sender = os.getenv("EMAIL")
    password = os.getenv("EMAIL_PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = "Daily Kolkata Weather Forecast"
    msg["From"] = sender
    msg["To"] = recipient

    body = "7-Day Kolkata Weather Forecast:\n\n"

    for day in forecast_data:
        body += f"{day['date']} → {round(day['avg_temp'],2)} °C\n"

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)