#Elfar Snær Arnarson
#09 September 2019
#Skilaverkefni 3
import random
import csv

#Listi búinn til, geymir svör og spurningar
spurningar = []

#Spurningar skjalið opnað
with open("spurningar.csv", "r") as f:
    reader = csv.reader(f, delimiter=";")
    #Skjalið lesi og fært yfir í lista
    for rod in reader:
        spurningar.append(rod)
        #lesari = csv.reader(spurningar.csv, delimiter=";")
        #spurningar = list(lesari)

#Listanum látinn breytast í hvert skipti sem hann er keyrður.
rndSpurningar = random.sample(spurningar, k=10)

#Telur upp í tíu, sama og fjöldi spurninga. Stöðvar svo while loopið.
teljari = 0
#Telur stiginn
stig = 0

#While breyta sem spyr spurningar þángað til að listinn er tæmdur.
while teljari != 10:
    #prenta út spurningu.
    print(rndSpurningar[teljari][0])
    #Læt svarið við spurningunni í streng
    svarid = rndSpurningar[teljari][1]
    #Strengur sem biður um inslátt svarsins frá notanda
    svar = input("Svarið þitt: ")
    #if breyta sem tékkar hvort fyrsta svarið er rétt.
    if svar == svarid:
        print("Rétt!")
        stig += 1
    #Ef svarið var ekki rétt í fyrstu reynir notandi aftur
    elif svar != svarid:
        svar = input("Rangt, reyndu aftur:")
        #Ef svarið er rétt þá fær notandi stig og loopið byrjar aftur.
        if svar == svarid:
            print("Rétt!")
            stig += 1
        #Ef svarið var rangt í annað skipti, þá fær notandi rétta svarið gefið upp.
        elif svar != svarid:
            print("Svörinn voru röng.")
            print("Rétta svarið er:", svarid)
    #Bætir við teljarann í byrjun, telur að tíu og fer svo úr while breytunni.
    teljari += 1
#Sýnir heildarstig notanda í lokinn.
print("Stigin þín voru:",str(stig)+"/10")
input("Ýttu á enter til þessa að loka forriti")

