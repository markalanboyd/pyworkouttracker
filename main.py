import dotenv
import os
import requests

# Constants
dotenv.load_dotenv()
APP_ID = "6130389d"
API_KEY = os.environ.get("API_KEY")

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 167
AGE = 36

url = "https://trackapi.nutritionix.com/v2/natural/exercise"

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


response = requests.post(url=url, json=params, headers=headers)

data = response.json()

print(data)