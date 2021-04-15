#Elfar Snær Arnarson
#Janúar 16 2018
#Æfingadæmi 1

ok = False
while ok == False:
    print("1. Sláðu inn texta streng")
    print("2. Lesa skrá")
    print("3. Hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        strengur = input("Sláðu inn textastreng: ")
        f = open("skra.txt", "a")
        f.write(strengur + " ")
        print(strengur,"hefur verið skrifaður í skránna skra.txt ")
        f.close()

    if val == 2:
        f = open("skra.txt", "r")
        print("Innihald skrárinnar skra.txt er:", f.read())

    if val == 3:
        ok = True