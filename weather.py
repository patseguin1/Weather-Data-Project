import csv
import statistics

# Import the data from the CSV file and read it into memory.
# The average temperature for the day is at index 4 in each row.
temps_2020 = []
with open("history_data_2020.csv") as file:
    reader = csv.reader(file)
    # Take off the top row because it contains the field names
    fields = next(reader)
    for row in reader:
        # Convert the temperature values from string to float.
        temps_2020.append(float(row[4]))

temps_2019 = []
with open("history_data_2019.csv") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        temps_2019.append(float(row[4]))

temps_2018 = []
with open("history_data_2018.csv") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        temps_2018.append(float(row[4]))

temps_2017 = []
with open("history_data_2017.csv") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        temps_2017.append(float(row[4]))

temps_2016 = []
with open("history_data_2016.csv") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        temps_2016.append(float(row[4]))

temps_2015 = []
with open("history_data_2015.csv") as file:
    reader = csv.reader(file)
    fields = next(reader)
    for row in reader:
        temps_2015.append(float(row[4]))

# Use the statistics.mean function to get the average of each list.
average_2020 = statistics.mean(temps_2020)
average_2019 = statistics.mean(temps_2019)
average_2018 = statistics.mean(temps_2018)
average_2017 = statistics.mean(temps_2017)
average_2016 = statistics.mean(temps_2016)
average_2015 = statistics.mean(temps_2015)

print("2020 average: {} degrees F".format(average_2020))
print("2019 average: {} degrees F".format(average_2019))
print("2018 average: {} degrees F".format(average_2018))
print("2017 average: {} degrees F".format(average_2017))
print("2016 average: {} degrees F".format(average_2016))
print("2015 average: {} degrees F".format(average_2015))
