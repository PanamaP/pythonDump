#Elfar Snær Arnarson

import csv

with open("postnumer.csv", "r") as csvFile:
    reader = csv.reader(csvFile, delimiter=";")
    for rod in reader:
        print(rod[0], "\t" , rod[1])
csvFile.close()


