import requests
from datetime import datetime
import csv

# Using Frankfurter API (free, no key)
URL = "https://api.frankfurter.app/latest?from=USD"

response = requests.get(URL)
data = response.json()

# print(data)

if "rates" not in data:
    print("API Error:", data)
    exit(1)

today = datetime.utcnow().strftime("%Y-%m-%d")
time = datetime.utcnow().strftime("%H:%M")

base = data["base"]
rates = data["rates"]

with open("currency.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    for target, rate in rates.items():
        writer.writerow([today, time, base, target, rate])

print("Currency rates saved.")

