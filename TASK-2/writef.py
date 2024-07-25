import csv

data = [["Name", "Age"], ["sarthak", 30], ["neekita", 25]]

with open("example.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
