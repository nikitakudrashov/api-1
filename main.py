import requests
import os
from dotenv import load_dotenv

load_dotenv("api_key")
TOKEN = os.getenv("TOKEN")
url = "https://calendarific.com/api/v2/holidays"
api_key = 'HRsefsCyLZ4bubXUVpZxSVlgmwpJOReV'
params = {
    "api_key":api_key,
    "country":"RU", 
    "year":"2025"
}

response = requests.get(url, params = params)
response.raise_for_status()
holidays = response.json()["response"]["holidays"]
months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентебря", "октября", "ноября", "декабря"]
for holiday in holidays:
    holiday_name = holiday["name"]
    holiday_description = holiday["description"]
    holiday_date = holiday["date"]["datetime"]
    day = holiday_date["day"]
    month = months[holiday_date["month"] - 1]
    print(f"Дата: {day} {month}")
    print(f"Название праздника: {holiday_name}")
    print(f"Описание: {holiday_description}")

