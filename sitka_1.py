import csv

open_file = open("sitka_weather_07-2018_simple.csv", r)

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)
