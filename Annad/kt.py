listi = [3, 2, 7, 6, 5, 4, 3, 2]

kt =    [1, 7, 0, 3, 0, 0, 3, 1]

reikn = 0*3 + 7*2 + 1*7 + 2*6 + 5*9 + 4*3 + 3*3 + 2*1

prufa = 0
for nr in range(1,11):
    prufa += listi[nr] * kt[nr]


s = reikn % 11

svarid = 11 - s


print(prufa)
print(reikn)
print(svarid)