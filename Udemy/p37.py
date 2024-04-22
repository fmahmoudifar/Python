import requests

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
  "token" : "65rfghu765gh87654",
  "username" : "fmahmoudifar",
  "agreeTermsOfService" : "yes",
  "notMinor" : "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)

print(response.text)

