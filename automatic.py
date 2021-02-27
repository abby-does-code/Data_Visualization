import csv
import matplotlib


open_file = open(input("What file are we looking at? "), "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)


lows = []

for index, header in enumerate(header_row):
    for row in csv_file:
    try:
        high = int(row[4])
        low = int(row[5])
    if header == "TMIN":
        for row in csv_file:
            lows.append(row())


print(lows)

"""
for row in csv_file:
    highs.append(int(row[5]))
    converted_date = dt.datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)
    lows.append(int(row[6]))     
   





fig1, a = plt.subplots(2)

a[0].plot(dates, highs, c="red")
a[1].plot(dates, lows, c="blue")

plt.show()
"""