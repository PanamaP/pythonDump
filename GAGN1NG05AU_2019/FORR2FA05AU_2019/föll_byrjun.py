#Elfar Snær Arnarson
#10 September 2019
#Skilaverkefni 2
import time
import random

#Bý til streng sem mun sjá til þess að while loopið muni halda áfram
ok = False

#Bý til while loop sem er tengt ok strengnum, prenta síðan út valmynd
while ok == False:
    print("1. Liður 1")
    print("2. Liður 2")
    print("3. Liður 3")
    print("4. Liður 4")
    print("5. Liður 5")
    print("6. Liður 6")
    print("7. Liður 7")
    print("8. Liður 8")
    print("9. Hætta")

    #Strengur sem tekur inn innslátt frá notanda um val hans
    val = int(input("Sláðu inn val: "))

    if val == 1:
        #Liður 1
        #Bý til fall sem breytir celsius yfir í fahrenheit
        def fahrenheit(celsius):
            return celsius * 1.8 + 32

        #Bý til fall sem breytir fahrenheit yfir í celsius
        def celsius(fahrenheit):
            return (fahrenheit - 32) / 1.8

        #Prenta út valmynd fyrir notanda um hvaða hitamælingu hann vilji breyta í
        print("í hvað viltu breyta?")
        print("1. Fahrenheit")
        print("2. Celsius")
        var = int(input("Sláðu inn val: "))

        #Bý til if breytu sem tékkar hvort notandi hafi valið að breyta í celsius
        if var == 1:
            #bý til streng sem tekur inn innslátt notanda, innsláttið fer svo í gegnum fallið
            celsius = float(input("Sláðu inn hita í Celsius: "))
            print(round(fahrenheit(celsius), 1))
        #Bý til sama hér og fyrir ofan, þetta er fyrir fahrenheit í celsius, öfugt við það fyrir ofan
        elif var == 2:
            fahrenheit = float(input("Sláðu inn hita í Fahrenheit: "))
            print(round(celsius(fahrenheit), 1))
        else: # else breyta sem tekur á móti vitlausum innslátti(inslátti sem eru ekki með if breytum)
            print('Vinsamlegast sláðu inn annaðhvort "1" eða "2".')
            print('Til að fara aftur í aðalvalmynd sláðu inn "q"')
            haetta = input(': ')
            if haetta == "q" or haetta == "Q":
                break

    if val == 2:
        # Liður 2
        #Bý til föll sem breyta frá celsius yfir í kelvin og öfugt
        def kelvin(celsius):
            return celsius + 273.15

        def celsius(kelvin):
            return kelvin - 273.15

        #Notandi spurður um aðgerð
        print("í hvað viltu breyta?")
        print("1. Kelvin")
        print("2. Celsius")
        var = int(input("Sláðu inn val: "))

        #if breytur búnar til, til að gá hvað notandi sló inn og vinna úr því rétt
        if var == 1:
            celsius = float(input("Sláðu inn hita í Celsíus: "))
            print(round(kelvin(celsius), 1))
        elif var == 2:
            kelvin = float(input("Sláðu inn hita í Kelvin: "))
            print(round(celsius(kelvin), 1), "°C")
        else:
            print('Vinsamlegast sláðu inn annaðhvort "1" eða "2".')
            print('Til að fara aftur í aðalvalmynd sláðu inn "q"')
            haetta = input(': ')
            if haetta == "q" or haetta == "Q":
                break

    if val == 3:
        #Liður 3
        #Fall búið til, til að gera veldisreikning
        def veldi(grunnTala,veldisTala):
            veldiReikningur = grunnTala ** veldisTala
            print(grunnTala, "í veldi", veldisTala, "er:", veldiReikningur)
            time.sleep(2)
        #Strengir búnir til, taka á móti innslátti notanda og láta í fallið
        grunnTala = int(input("Grunntala:"))
        veldisTala = int(input("Veldistala: "))

        veldi(grunnTala, veldisTala)

    if val == 4:
        # Liður 4
        #Föll búinn til, breyta tommum yfir í sentimetra og öfugt
        def tommur(sentimeter):
            return sentimeter / 2.54

        def sentimeter(tommur):
            return tommur * 2.54
        #Prentað út valmynd fyrir notanda
        print("í hvað viltu breyta?")
        print("1. Tommur")
        print("2. Sentimetra")
        var = int(input("Sláðu inn val: "))
        #if breytur sem vinna úr innslátti notanda
        if var == 1:
            sentimeter = float(input("Sláðu inn sentimetra: "))
            print(round(tommur(sentimeter), 2),)

        elif var == 2:
            tommur = float(input("Sláðu inn tommur: "))
            print(round(sentimeter(tommur), 2),"cm")
        else:
            print('Vinsamlegast sláðu inn annaðhvort "1" eða "2".')
            print('Til að fara aftur í aðalvalmynd sláðu inn "q"')
            haetta = input(': ')
            if haetta == "q" or haetta == "Q":
                break

    if val == 5:
        #Föll búinn til, breyta líter yfir í gallon og öfugt
        def liter(gallon):
            return gallon * 3.785

        def gallon(liter):
            return liter / 3.785
        #Valmynd fyrir notanda
        print("Hvað viltu breyta?")
        print("1. Líter")
        print("2. Gallon")
        var = int(input("Sláðu inn val: "))
        #Innsláttur lesinn og unninn
        if var == 1:
            gallon = float(input("Sláðu inn gallon: "))
            print(round(liter(gallon),2),"L")

        elif var == 2:
            liter = float(input("Sláðu inn lítra: "))
            print(round(gallon(liter), 2))
        else:
            print('Vinsamlegast sláðu inn annaðhvort "1" eða "2".')
            print('Til að fara aftur í aðalvalmynd sláðu inn "q"')
            haetta = input(': ')
            if haetta == "q" or haetta == "Q":
                break

    if val == 6:
        #Föll búinn til fyrir hvert kyn.
        def kvenkyn(kvk):
            print("Sæl og blessuð" + ", " + nafn)

        def karlkyn(kk):
            print("Sæll og blessaður" + ", " + nafn)
        #Strengir búnir til sem byðja um kyn og nafn.
        kyn = input("Kyn(kvk/kk): ")
        nafn = input("Hvað heitir þú? : ")
        #if breyta búinn til, tékkar á hvaða kyn var slegið inn og dregur upp viðeigandi fall.
        if kyn == "kvk" or kyn == "KVK":
            kvenkyn(nafn)
            time.sleep(2)
        elif kyn == "kk" or kyn == "KK":
            karlkyn(nafn)
            time.sleep(2)
        else:
            print("Vitlaust slegið inn.")
            time.sleep(1)

    if val == 7:
        #Bý til fall sem býr til random tölu
        def kasta():
            print("-----------------")
            print("Random heiltala:", random.randint(1, 7))
            print("-----------------")
            time.sleep(1)

        kasta()

    if val == 8:
        #Bý til fall sem tekur inn tvo lista, finnur síðan hvaða tölur eru eins og lætur þær í nýjan lista.
        def mismunur(listi1, listi2):
            listi3 = []
            for x in listi1:
                if x in listi2:
                    listi3.append(x)
            print("Tölur sem eru eins í báðum listum:", listi3)
            time.sleep(2)
        #Listar geta verið núþegar tilbúnir eða búnir til úr innslátti notanda
        listi1 = [1, 2, 3, 4, 5]
        listi2 = [2, 4, 5]

        #Fall kallað með nú þegar tilbúna lista
        mismunur(listi1,listi2)

    if val == 9:
        #Stoppar while loopið og lokar forritun.
        break

