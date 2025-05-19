# with open("Udemy/p25/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)


#######################

# import csv

# with open("Udemy/p25/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

############################

import pandas

data = pandas.read_csv("Udemy/p25/weather_data.csv")
print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)




avg = sum(temp_list) / len(temp_list)
print(avg)

print(data["temp"].mean())

print(data["temp"].max())

print(data.condition)

print(data[data.day == 'Monday'])

print(data[data.temp == data.temp.max()])
 
monday = data[data.day == 'Monday']
print(monday.condition)

####################################

data = pandas.read_csv("Udemy/p25/2018.csv")
gray_squirrels = data[data["Primary Fur Color"] == "Gray"]
print(gray_squirrels)