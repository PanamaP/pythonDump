#Elfar Snær Arnarson
#05 Nóvember 2019
#Tímaverkefni 2


listi = ["Einn", "Tveir", 'Abba', "Og", 'Tort', 'er']

tegund = {
        'Bíll 1': 'Toyota',
        "Bíll 2": 'Honda',
        "Bíll 3": 'Ford',
        "Bíll 4": 'Kia',
        "Bíll 5": 'Benz',
        "Bíll 6": 'Suzuki',
        "Bíll 7": 'Hyundai'
    }

def match_ends(words):
    listi = []
    for word in words:
        if len(word) >= 2 and word[0].lower() == word[-1]:
            listi.append(word.capitalize())
    return listi

def billtegund(tegund):
    for key in tegund.keys():
        print(key, "er", tegund[key])


def billtegundLengd(tegund):
    listi = []
    for key in tegund.keys():
        if len(tegund[key]) <= 4:
            listi.append(tegund[key])
    return listi

def dictionary():
    listi = []
    reikn = {
        'a': '1',
        'b': '2',
        'c': '3',
        'd': '4',
        'e': '5'
    }
    nafn = input("Sláðu inn nafn: ")
    for stafur in nafn:
        if stafur in reikn.keys():
            listi.append(reikn[stafur])
    teljari = 1
    for x in listi:
        if teljari < len(listi):
            print(x, end="")
            teljari += 1
        else:
            print(x)
            teljari = 0



ok = False
while ok == False:
    print("1. A list")
    print("2. B Tuple")
    print("3. C Dictionary")

    val = int(input("Sláðu inn val(Tölu): "))

    if val == 1:
        print('Listinn með strengjunum er:')
        print(listi)
        print("Strengir lengri en tveggja stafa og fyrsti og seinasti stafur er eins:")
        for ord in match_ends(listi):
            print(ord)

    if val == 2:
        billtegund(tegund)

        print("Bílategundir sem hafa 4 eða færri stafi í heiti:")
        for bill in billtegundLengd(tegund):
            print(bill)


    if val == 3:
        dictionary()

