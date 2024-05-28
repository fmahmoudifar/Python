import requests

APP_ID = "1dc14766"
API_KEY = "b3dbb023937dda383c557aee25735d81"

#SHEET_ENDPOINT
#USERNAME
#PASSWORD
#TOKEN


exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/nutrients"

headers= {
    "Content-Type": "application/json",
    "x-app-id": APP_ID  ,
    "x-app-key": API_KEY
  } # type: ignore

response = requests.post(url=exercise_endpoint, headers=headers, json={
    "query": input("Tell me what did you eat: ")
})
print(response.text)