#Elfar Snær Arnarson
#13 Feb 2020
#Tímaverkefni 1 Valmynd

from Timaverkefni_1.Timaverkefni1 import CheckingAccount

checkingAcc = CheckingAccount()

ok = False
while ok == False:
    print('1. Balance')
    print('2. Debit/Withdraw')
    print('3. Credit/Deposit')
    print('4. Quit')
    val = int(input('Type in your choice: '))
    if val == 1:
        checkingAcc.prentaBalance()
    if val == 2:
        checkingAcc.debit()
    if val == 3:
        checkingAcc.credit()
    if val == 4:
        break
    else:
        print("Wrong Input, Try Again")

