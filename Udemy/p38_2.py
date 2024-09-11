import requests

url = 'https://api.sheety.co/cd7e1592ba1cbb02b87aa44565d6f5e9/myWorkouts/workouts'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    # Do something with the data
    print(data['workouts'])
else:
    print("Failed to retrieve data:", response.status_code)
