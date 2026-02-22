import requests
import csv
from datetime import datetime

API_KEY = "YOUR_API_KEY"
CITY = "Bratislava"

URL = f"https://api.openweathermap.org/data/2.5/weather?q=Bratislava&appid=db715d0af3dbc1308a640aa3fbe3f599&units=metric"

response = requests.get(URL)
data = response.json()

now = datetime.utcnow()

row = [
    now.strftime("%Y-%m-%d"),
    now.strftime("%H:%M"),
    data["main"]["temp"],
    data["main"]["humidity"],
    data["wind"]["speed"],
    data["weather"][0]["description"]
]

with open("weather.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(row)

print("Saved weather.")
