import requests
from datetime import datetime

pixela_endpoint = 'https://pixe.la/v1/users'
USERNAME = 'fmahmoudifar'
TOKEN = '65rfghu765gh87654'
GRAPH_ID = 'graph1'

user_params = {
  "token" : TOKEN,
  "username" : USERNAME,
  "agreeTermsOfService" : "yes",
  "notMinor" : "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

graph_config = {
  "id" : GRAPH_ID,
  "name" : "Cycling Graph",
  "unit" : "Km",
  "type" : "float",
  "color" : "ajisai"
}

headers = {
  "X-USER-TOKEN" : TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
print(today.strftime("%Y%m%d"))

date = today.strftime("%Y%m%d")
pixela_data = {
  "date" : today.strftime("%Y%m%d"),
  "quantity" : "6.6"
}

#esponse = requests.post(url=pixela_creation_endpoint, json=pixela_data, headers=headers)
#print(response.text)


update_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

new_pixela_data = {
  "quantity" : "1.5"
}

#response = requests.put(url=update_enpoint, json=new_pixela_data, headers=headers)
#print(response.text)

delete_enpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

response = requests.delete(url=delete_enpoint, headers=headers)
print(response.text)