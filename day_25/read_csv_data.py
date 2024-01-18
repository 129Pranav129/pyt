# import csv

# temp=[]
# with open("C:\\pyt\\day_25\\weather_data.csv") as file:
#     data = csv.reader(file)
#     print(data)

#     for i in data:
#         print(i)
#         if(i[1]!="temp"):
#             temp.append(int(i[1]))

#     print(temp)        

import pandas

data = pandas.read_csv("C:\\pyt\\day_25\\weather_data.csv")
# print(data["temp"])

print(data)

#get th temp from tues and convert to Fahrenhite'

data_row= data[data.day=="Tuesday"]
print(data_row)
tempC = data_row.temp[1]  
print(tempC)

