import requests

GENDER = 'male'
WEIGHT_KG = 75
HEIGHT_CM = 178
AGE = 41

APP_ID = "1dc14766"
API_KEY = "b3dbb023937dda383c557aee25735d81"

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

response = requests.post(exercise_endpoint, headers=headers, json=parameters)
result = response.json()
print(result)