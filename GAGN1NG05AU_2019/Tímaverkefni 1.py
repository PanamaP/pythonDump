#Elfar Snær Arnarson
#16 September 2019
#Tímaverkefni 1
import csv
import pandas as pd

ok = False
while ok == False:
    print("1. Bæta í skrána")
    print("2. Birta skrána í heild")
    print("3. Birta upplýsingar um ákveðið dýr eftir nafni")
    print("4. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        with open("Gaeludyr.txt", "a", encoding="utf-8") as f:
            nafn = input("Sláðu inn nafn: ")
            nafnDyr = input("Sláðu inn nafn gæludýrsins: ")
            tegund = input("Sláðu inn tegund dýrsins: ")

            texti = nafn + ";" + nafnDyr + ";" + tegund + "\n"
            f.write(texti)

    if val == 2:
        with open("Gaeludyr.txt", "r+", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            print("------------------------------")
            print("Eigandi", "\t", "  ", "Nafn Dýrsins", "\t", "Tegund")
            print()
            for rod in reader:
                print(rod[0], "\t", "\t" + rod[1], "\t", "\t", "\t", rod[2])
            print("------------------------------")


    if val == 3:
        skra = open("Gaeludyr.txt", "r+", encoding="utf-8")
        allir = []

        for line in skra:
            l = line.split(";")
            allir.append(l)

        nafn = input("Skrifaðu nafn eiganda: ")

        for eigandi in allir:
            if eigandi[0] == nafn:
                print("Eigandi:", nafn)
                print("Nafn Dýrsins:", eigandi[1])
                print("Tegund:", eigandi[2])

    if val == 4:
        break