str = input("Sláðu inn setningu: ")
wordlist = str.split()
for i in range(len(wordlist)):
    if len(wordlist[i]) <= 3:
        wordlist[i] = wordlist[i].lower()
    elif len(wordlist[i]) >= 7:
        wordlist[i] = wordlist[i].upper()
for i in range(len(wordlist)):
    print(wordlist)

def word_mixer(wordlist):
