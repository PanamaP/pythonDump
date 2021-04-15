#Elfar Snær Arnarson
#23 Janúar 2019
#Skilaverkefni 2

ok = False
while ok == False:
    print("1. Bæta við nýjum í símaskrána")
    print("2. Breyta upplýsingum í símaskránni")
    print("3. Eyða upplýsingum / eyða línu úr símaskránni")
    print("4. Prenta út alla símaskrána ein lína per notanda")
    print("5. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        nafn = input("Sláðu inn nafn: ")
        simanumer = input("Sláðu inn símanúmer: ")
        f = open("simaskra.txt", "a")
        f.write(nafn + ";" + simanumer + "\n")
        print(nafn,"hefur verið bætt við í skránna simaskra.txt ")
        f.close()

    if val == 2:
        f = open("simaskra.txt", "r")
        data = f.readlines()
        print(data)
        Lina = int(input("Hvaða línu viltu breyta?: "))
        data[Lina] = 
        print(data)







    if val == 5:
        ok = True


        breyta = int(input("Hvern á að breyta? Veldu eftir tölu: "))
        breyta -= 1
        rett = input("Þú valdir, " + listi[breyta] + " Er það rétt? Já/Nei?")
        f = f.replace(listi[breyta], )
        s = open("simaskra.txt", "w")
        f.write(s)
        f.close()