import requests
import datetime as dt
import os

# API_KEY = "8f16a578351f150d76772f1744a2580a"
# APP_ID = "da7727e8"
# API_ENDPOINT = "https://trackapi.nutritionix.com/v2"
# SHEETY_ENDPOINT = "https://api.sheety.co/c66f910988a4ff3e72e325581e147ebb/myWorkout/sheet1"
# exercise_endpoint = f"{API_ENDPOINT}/natural/exercise"

GENDER = "Female"
WEIGHT_KG = 55
HEIGHT_CM = "5.6"
AGE = "22"

APP_ID = os.environ.get("APP_ID", "Does not exist")
API_ENDPOINT = os.environ.get("API_ENDPOINT", "Does not exist")
API_KEY = os.environ.get("API_KEY", "Does not exist")
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT", "Does not exist")
exercise_endpoint = os.environ.get("exercise_endpoint", "Does not exist")


# basic = HTTPBasicAuth('user', 'pass')
# requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)

text = input("What are the exercises that you have done?\n")

exercise_params = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

header = {
    "x-app-key": API_KEY,
    "x-app-id": APP_ID,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=header)
data = response.json()["exercises"]

now = dt.datetime.now()
today = now.strftime("%d/%m/%Y")
now_time = now.strftime("%H:%M:%S")

sheety_headers = {
    "Authorization": "Basic YWVyZXg6QWVyZXhAMTIzNDU2"
}

get_response = requests.get(url=SHEETY_ENDPOINT, headers=sheety_headers)

for status in data:
    post_params = {
        "sheet1": {
            "date": today,
            "time": now_time,
            "exercise": status["name"].title(),
            "duration": status["duration_min"],
            "calories": status["nf_calories"],
        }
    }

    post_response = requests.post(url=SHEETY_ENDPOINT, json=post_params, headers=sheety_headers)

