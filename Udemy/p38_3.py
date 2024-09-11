import requests
import json

url = 'https://api.sheety.co/cd7e1592ba1cbb02b87aa44565d6f5e9/myWorkouts/workouts'
headers={"Content-Type": "application/json"}
body = {
    "workout": {
        'date': '21/07/2020',
        'time': '15:00:00',
        'exercise': 'Running',
        'duration': 22,
        'calories': 130,
    }
}
response = requests.post(url, headers=headers, json=body)

#response = requests.post(url, data=json.dumps(body), headers=headers)

result = response.json()
print(result)