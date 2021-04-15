#Elfar Snær Arnarson
#26 Ágúst 2019
#Æfingadæmi 2

ok = False
while ok == False:
    print("1. Gögn Skrifuð")
    print("2. Gögn Lesin")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        f = open("tolur.txt", "w")
        for i in range(5):
            tala = int(input("Sláðu inn tölu: "))
            f.write(str(tala)+" ")


    if val == 2:
        f = open("tolur.txt", "r")
        innihald = f.read()
        f.close()

        #Það sem ég fann
        listi = innihald.split()
        sum = 0
        for num in listi:
            sum += int(num)
        medaltal = sum/len(listi)
        print("Meðaltal:", round(medaltal, 2))




        #það sem kennarinn kom með
        """innihald = f.read()
        f.close()

        listi = innihald.split(", ")
        listi.pop()

        listi = list(map(int, listi))

        medatal = sum(listi)/len(listi)
        print(round(medatal, 2))"""

    if val == 3:
        ok = True


