# import csv
import pandas

# def get_data(file_name):

#     with open(file_name) as file:
#         data = csv.reader(file)
#         temperatures = []
#         for row in data:
#             if row[1] != "temp":
#                 temperatures.append(int(row[1]))
#         print(temperatures)
#         file.close()
#         return data

# get_data("weather_data.csv")

# def get_average_temp(temps):
#     total_temp = 0
#     num_temps = len(temps)
#     for temp in temps:
#         total_temp += temps[temp]
#     return round(total_temp/num_temps, 2)

# data = pandas.read_csv("weather_data.csv")

# data_dict = data.to_dict()
# data_list = data['temp'].to_list()

# print(get_average_temp(data_dict['temp']))

# average_temp = round (sum(data_list) / len(data_list), 2)
# print(average_temp)

# print("average temp: ", round(data['temp'].mean(), 2))
# print("max temp: ", data['temp'].max())

# max_temp = data['temp'].max()
# max_temp_day = data[data.temp == max_temp].day.to_list()[0]
# print("max-temp-day:")
# print(data[data.day == max_temp_day])

# temp_monday = int(data[data.day == "Monday"].temp)
# temp_monday_in_farenheight = round(temp_monday * 9 / 5 + 32, 2)
# print("temp in farenheight, monday: ", temp_monday_in_farenheight) 

# data_dict_2 = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict_2)
# data.to_csv("new_data.csv")

from math import isnan

data = pandas.read_csv("squirrel_data.csv")
data_dict = data.to_dict()

fur_types = data['Primary Fur Color'].to_list()
unique_types = []
count_types = []
for fur in fur_types:
    if not(unique_types.__contains__(fur)) and type(fur) == str:
        unique_types.append(fur)
    # elif len(unique_types) > 0 and fur == unique_types[0]:
    #     count_types[0] += 1
    # elif len(unique_types) > 1 and fur == unique_types[1]:
    #     count_types[1] += 1
    # elif len(unique_types) > 2 and fur == unique_types[2]:
    #     count_types[2] += 1
print(unique_types)
 
for fur_color in unique_types:
  count_types.append(len(data[data['Primary Fur Color'] == fur_color]))

data_squirrel = { "Fur Color": unique_types, 
                  "Count": count_types}

new_data = pandas.DataFrame(data_squirrel)
new_data.to_csv("squirrel_count.csv")