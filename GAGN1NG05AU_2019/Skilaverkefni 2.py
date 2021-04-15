#Elfar Snær Arnarson
#28 Ágúst 2019
#Skilaverkefni 2
import csv


ok = False
while ok == False:
    print("1. Bæta við nýjum í símaskrána.")
    print("2. Breyta upplýsingum í símaskránni.")
    print("3. Eyða upplýsingum / eyða línu úr símaskránni.")
    print("4. Prenta út símaskrá")
    print("5. Hætta í forritinu.")
    val = int(input("Hvað er valið: "))

    if val == 1:
        with open("Símaskrá.txt", "a", encoding="utf-8") as f:
            nafn = input("Sláðu inn nafn: ")
            kennitala = input("Sláðu inn kennitölu: ")
            simanr = input("Sláðu inn Símanúmer: ")

            text = kennitala+";"+nafn+";"+simanr+"\n"
            f.write(str(text))

    if val == 2:
        skra = open("Símaskrá.txt", "r+", encoding="utf-8")
        allir = []
        for line in skra:
            lina = line.split(";")
            allir.append(lina)
        skra.close()

        with open("Símaskrá.txt", "r", encoding="utf-8") as f:
            print('\t' + "Kt" + '\t' + "\t" + " " + "Nafn" + "\t " + "\t" + "   " + "  " + 'Símanúmer')
            print("---------------------------------------")
            reader = csv.reader(f, delimiter=";")
            for rod in reader:
                print(rod[0], "\t", rod[1], "\t", rod[2])
            print("---------------------------------------")
        f.close()

        kennitala = input("Sláðu inn kt þess sem þú vilt breyta: ")
        nafn = input("Sláðu inn breytingu á nafni: ")
        simi = input("Sláðu inn annað símanúmer: ")
        teljari = 0
        for i in allir:
            if i[0] == kennitala:
                allir[teljari][0] = kennitala
                allir[teljari][1] = nafn
                allir[teljari][2] = simi
                break
            else:
                teljari = teljari + 1
        f = open("Símaskrá.txt", "w", encoding="utf-8")
        phone = ""
        for x in allir:
            phone = x[2].replace("\n", "")
            texti = x[0] + ";" + x[1] + ";" + phone + "\n"
            f.write(texti)
        f.close()
        print()


    if val == 3:
        skra = open("Símaskrá.txt", "r+", encoding="utf-8")

        allir = []
        for line in skra:
            lina = line.split(";")
            allir.append(lina)
        skra.close()

        with open("Símaskrá.txt", "r", encoding="utf-8") as f:
            print('\t' + "Kt" + '\t' + "\t" + " " + "Nafn" + "\t " + "\t" + "   " + "  " + 'Símanúmer')
            print("---------------------------------------")
            reader = csv.reader(f, delimiter=";")
            for rod in reader:
                print(rod[0], "\t", rod[1], "\t",rod[2])
            print("---------------------------------------")
        f.close()

        kennitala = input("Sláðu inn kt þess sem þú vilt eyða: ")

        teljari = 0
        for i in allir:
            if i[0] == kennitala:
                del allir[teljari]
                break
            else:
                teljari = teljari + 1

        f = open("Símaskrá.txt", "w", encoding="utf-8")
        simi = ""
        for x in allir:
            simi = x[2].replace("\n", "")
            texti = x[0] + ";" + x[1] + ";" + x[2]
            f.write(texti)
        f.close()


    if val == 4:
        with open("Símaskrá.txt", "r", encoding="utf-8") as f:
            print('\t' + "Kt" + '\t' + "\t" + " " + "Nafn" + "\t " + "\t" + "   " + "  " + 'Símanúmer')
            print("---------------------------------------")
            reader = csv.reader(f, delimiter=";")
            for rod in reader:
                print(rod[0], "\t", rod[1], "\t",rod[2])
            print("---------------------------------------")
        f.close()

        '''f = open("Símaskrá.txt", "r", encoding="utf-8")
        print('\t' + "Kt" + '\t' + "\t" + "  " + "Nafn" + "\t " + "" + 'Símanúmer')
        for l in f:
            nytt = l.split(";")
            print(nytt, "")
        f.close()'''

    if val == 5:
        break