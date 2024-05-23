import requests 

api_key = "0SW0F8JJKSV2TNIU"

stock_endpoint = "https://www.alphavantage.co/query"
news_endpoint = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "BTC",
    "apikey": api_key
}

response = requests.get(stock_endpoint, params=stock_params)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
T1_data = data_list[0]
T1_COP = T1_data["4. close"]
print(T1_COP)

T2_data = data_list[1]
T2_COP = T2_data["4. close"]
print(T2_COP)

difference = float(T1_COP) - float(T2_COP)
print(difference)

diff_percetage = abs((difference / float(T1_COP)) * 100)
print(diff_percetage)

if diff_percetage > 0:
  print("get news")
