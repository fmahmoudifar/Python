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