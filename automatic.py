import csv
import matplotlib


open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)


for index, header in enumerate(header_row):
    if header_row["header"] == "TMIN":
        lows_index_no = header[index]

# String indices must be integers or slices, not str
# String index out of range

print(lows_index_no)

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