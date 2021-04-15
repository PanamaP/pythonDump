# Elfar Snær Arnarson
# 15 Janúar 2020
# Skilaverkefni 2


import csv
from klasi import Verkalydsfelag

verkalydsfelag = []


def opnaSkra():
    with open("verkalydsfelag.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            hlutur = Verkalydsfelag(row[0], row[1], row[2], row[3])
            verkalydsfelag.append(hlutur)
    return verkalydsfelag

def skrifaSkra():
    with open("verkalydsfelag.csv", "w", newline="", encoding="utf-8") as file:
        for hlutur in verkalydsfelag:
            line = hlutur.nafn + ";" + hlutur.felagsnumer + ";" + hlutur.laun + ";" + \
                   hlutur.kennitala + "\r\n"
            file.write(line)

def nyrMedlimur():
    nafn = input("Nafn: ")
    felagsnumer = input("Félagsnúmer: ")
    laun = input("Laun: ")
    kennitala = input("Kennitala: ")
    hlutur = Verkalydsfelag(nafn, felagsnumer, laun, kennitala)
    verkalydsfelag.append(hlutur)


def eydaMedlimi():
    tala = 0
    with open("verkalydsfelag.csv", "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            tala += 1
            Verkalydsfelag(row[0], row[1], row[2], row[3])
            print(f"{tala}. {row[0]}\n   félagsnúmer: {row[1]}\n")

    index = -1
    eyda = input(f"Hverjum viltu eyða? [Félagsnúmer]: ")
    for medlimur in verkalydsfelag:
        index += 1
        if medlimur.felagsnumer == eyda:
            hver = medlimur.nafn
            felags = medlimur.felagsnumer
            del verkalydsfelag[index]
    print(hver,", Félagsnúmer:", felags, "- Hefur verið eytt.")


def breytaMedlimi():
    launbreyta = input("Félagsnúmer: ")
    nylaun = input('Breyting á launum: ')
    for medlimur in verkalydsfelag:
        if medlimur.felagsnumer == launbreyta:
            medlimur.laun = nylaun

def prentaVerkalydsfelag():
    for hlutur in verkalydsfelag:
        hlutur.prenta_upplysingar_um_medlim()

def nafnLaun():
    for hlutur in verkalydsfelag:
        print(f"Nafn: {hlutur.nafn}\nLaun: {hlutur.laun}\n")

def utborgudLaun():
    for hlutur in verkalydsfelag:
        print(f'Nafn: {hlutur.nafn}\nútborguð laun: {round(hlutur.utborgud_laun())}\n')

def heildarskattar():
    skattur = 0
    for hlutur in verkalydsfelag:
        skattur += hlutur.skatt()
    print(f"Heildarskattur allra: {round(skattur)}")

opnaSkra()
ok = False
while not ok:
    print('1. Prenta Verkalydsfelag')
    print('2. Bæta við nýjum meðlim')
    print('3. Eyða meðlim')
    print('4. Breyta meðlim')
    print('5. Prenta Nafn og laun alla meðlima')
    print('6. Prenta útborguð laun hvers meðlimar')
    print('7. Prenta heildarskatta allra meðlima')
    print('8. Hætta')
    val = int(input('Sláðu inn val: '))

    if val == 1:
        prentaVerkalydsfelag()
    elif val == 2:
        nyrMedlimur()
    elif val == 3:
        eydaMedlimi()
    elif val == 4:
        breytaMedlimi()
    elif val == 5:
        nafnLaun()
    elif val == 6:
        utborgudLaun()
    elif val == 7:
        heildarskattar()
    elif val == 8:
        break
    skrifaSkra()



