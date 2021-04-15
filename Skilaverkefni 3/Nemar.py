# Elfar Snær Arnarson
# 27 Janúar 2020
# Skilaverkefni 3

import pickle


class Nemi:
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang):
        self.kt = kt
        self.nafn = nafn
        self.kyn = kyn
        self.heimilisfang = heimilisfang
        self.simanumer = simanumer
        self.netfang = netfang


class Grunnskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, forradarmadur, nafnSkola):
        super().__init__(kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.forradarmadur = forradarmadur
        self.nafnSkola = nafnSkola


class Framhaldsskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, brautarheiti, busetustyrk):
        super().__init__(kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.brautarheiti = brautarheiti
        self.busetustyrk = busetustyrk



class Haskolanemi(Nemi):
    def __init__(self, kt, nafn, kyn, heimilisfang, simanumer, netfang, stigNams, namslan):
        super().__init__(kt, nafn, kyn, heimilisfang, simanumer, netfang)
        self.stigNams = stigNams
        self.namslan = namslan


nemendalisti = []
# skraningnemenda = nemar.SkraningNemenda()
#óklárað
choice = "0"
while choice != "7":
    print("1. Opna nemaskrá")
    print("2. Skrá grunnskólanema.")
    print("3. Skrá framhaldsskólkanema.")
    print("4. Skrá Háskólanema.")
    print("5. Vista nemaskrá")
    print("6. Prenta nemendalista")
    print("7. Hætta")

    choice = str(input("Sláðu inn val: "))
    if choice == "1":
        with open('nema_listi', 'rb') as file:
            nemendalisti = pickle.load(file)
    elif choice == "2":
        grunnskolanemi = Grunnskolanemi('2905992379', 'Jón Arnar Árnason', 'kk', 'Svarthamar 26', '58712345',
                                             'jonarnar@gmail.com', 'Árni Árnason', 'Borgarskóli')
        nemendalisti.append(grunnskolanemi)
    elif choice == "3":
        framhaldsskolanemi = Framhaldsskolanemi('2815005485', 'Arnar Sigurðsson', 'kk', 'Logafold 13'
                                                , '5874584', 'arnarsig@gmail.com', 'Tölvubraut', 'Nei')
        nemendalisti.append(framhaldsskolanemi)
    elif choice == "4":
        haskolanemi = Haskolanemi('2504884828', 'Snæbjörn Fjarðarsson', 'kk', "Dúfnahóll 14"
                                  , '8485784', "snaebjorn12@gmail.com", 'PHd', 'Já')
        nemendalisti.append(haskolanemi)
    elif choice == "5":
        with open("nema_listi", 'wb') as file:
            pickle.dump(nemendalisti, file)
    elif choice == "6":
        #óklárað
        print(nemendalisti)
