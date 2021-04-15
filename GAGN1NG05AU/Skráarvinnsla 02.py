#Elfar Snær Arnarson
# 16 Janúar 2018
#Æfingarverkefni 02

ok = False
while ok == False:
    print("1. Gögn skrifuð í skrá: ")
    print("2. Gögn lesin úr skrá: ")
    print("3. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        print("Sláðu inn fimm einkunnir.")
        f = open("Einkunnir.txt", "w")
        for x in range(0,5):
            einkunn = int(input("Einkunn: "))
            if x != 4:
                f.write(str(einkunn) + ", ")
            else:
                f.write(str(einkunn))
        f.close()

    if val == 2:
        f = open("Einkunnir.txt", "r")
        innihald = f.read()
        listi = innihald.split(", ")
        #print(listi)
        #print(int(listi[0]))
        summa = 0
        for x in listi:
            summa += int(x)
        medaltal = summa/len(listi)
        print(round(medaltal, 2))

    if val == 3:
        break

