import requests
from datetime import datetime

# Fixed Kolkata coordinates
LAT = 22.5726
LON = 88.3639

def generate_forecast():

    api_url = (
        "https://api.open-meteo.com/v1/forecast?"
        f"latitude={LAT}&longitude={LON}"
        "&daily=temperature_2m_max,temperature_2m_min"
        "&timezone=auto"
    )

    response = requests.get(api_url).json()

    if "daily" not in response:
        raise Exception("Weather API failed")

    dates = response["daily"]["time"]
    max_temps = response["daily"]["temperature_2m_max"]
    min_temps = response["daily"]["temperature_2m_min"]

    forecast_data = []

    for i in range(7):
        avg_temp = (max_temps[i] + min_temps[i]) / 2

        forecast_data.append({
            "date": dates[i],
            "avg_temp": avg_temp
        })

    return forecast_data