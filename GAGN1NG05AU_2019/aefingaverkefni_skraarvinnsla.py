#Elfar Snær Arnarson
#26 Ágúst 2019

ok = False
while ok == False:
    print("1. Sláðu inn textastreng")
    print("2. Innihald skráar")
    print("3. til að hætta")
    val = int(input("Sláðu inn val: "))

    if val == 1:
        texti = input("Skrifaðu inn texta: ")
        f = open("skra.txt", "a", encoding = "utf-8")
        f.write(texti)
        f.close()

    if val == 2:
        f = open("skra.txt", "r", encoding = "utf-8")
        print("Innihald skáar er:" , f.read())
        f.close()

    if val == 3:
        ok = True
