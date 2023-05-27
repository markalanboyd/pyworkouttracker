import dotenv
import os
import requests
import datetime as dt

dotenv.load_dotenv()
APP_ID = "6130389d"
API_KEY = os.environ.get("API_KEY")

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 167
AGE = 36

nutritionix_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": query,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_url,
                         json=params,
                         headers=headers,
                        )

data = response.json()

print(data)

SHEETY_URL = ("https://api.sheety.co/"
              "b5bd9b59860939d4e9861eda7da0941d/"
              "myWorkouts/workouts")

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")

headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
}

exercise_data = {}

for exercise in data["exercises"]:
    exercise_data = {
        "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    response = requests.post(url=SHEETY_URL,
                            headers=headers,
                            json=exercise_data,
                            )
    print(response.text)
