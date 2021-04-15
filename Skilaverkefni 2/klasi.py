# Elfar Snær Arnarson
# 15 Janúar 2020
# Skilaverkefni 2

class Verkalydsfelag:
    def __init__(self, nafn, felagsnumer, laun, kennitala):
        self.nafn = nafn
        self.felagsnumer = felagsnumer
        self.laun = laun
        self.kennitala = kennitala

    # reikna skatt medlims
    def skatt(self):
        return int(self.laun) * 0.36  # skattur 36%

    # reikna útborguð laun
    def utborgud_laun(self):
        return int(self.laun) - (self.skatt())  # Útborguð laun

    # prentar út upplýsingar
    def prenta_upplysingar_um_medlim(self):
        print(f"Nafn: {self.nafn}\nFélagsnúmer: {self.felagsnumer}\n"
              f"Laun: {self.laun}\nKennitala: {self.kennitala}")





