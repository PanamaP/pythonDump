peng = 100000
pengInnlegg = 100000

manadarInnlegg = 5000

vextir = 1.01
vextirReikn = 0.01


vextirCount = 0
vextirCountInnlegg = 0

print(round(peng, 0), "ISK")
for manudur in range(1, 13):

    peng = vextir*peng
    vextirPeng = vextirReikn * peng
    vextirCount += vextirPeng

    pengInnlegg = vextir * pengInnlegg + manadarInnlegg
    vextirInnlegg = vextirReikn * pengInnlegg
    vextirCountInnlegg += vextirInnlegg

    print(round(peng), "ISK", "-", 'vextir:', round(vextirPeng), "|", "+" + str(manadarInnlegg), ":",
          round(pengInnlegg), "ISK", '-', "vextir:", round(vextirInnlegg), "ISK", '-', manudur)

    if manudur == 12:
        eign = round(pengInnlegg)
        print("Vextir í heild: ")
        print("Án Innleggs:", round(vextirCount), 'ISK', '-', 'Með Innlegg:', round(vextirCountInnlegg), 'ISK')
        print("Greitt Innlegg:", 12 * manadarInnlegg)
        print("Upphæð lögð inn án vaxtar:", round(eign - vextirCountInnlegg))