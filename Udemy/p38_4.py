import requests
from datetime import datetime
# import os


GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 178
AGE = 41

APP_ID = "1dc14766"

API_KEY = "b3dbb023937dda383c557aee25735d81"

sheet_endpoint = 'https://api.sheety.co/cd7e1592ba1cbb02b87aa44565d6f5e9/myWorkouts/workouts'

# APP_ID = os.environ["APP_ID"]
# API_KEY = os.environ["API_KEY"]
# sheet_endpoint = os.environ["SHEET_ENDPOINT"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
    
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
# print (result)

################### Start of Step 4 Solution ######################

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    headers = {

        "Authorization": "Bearer FarshadTest"
    }

    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)