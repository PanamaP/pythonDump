# Elfar Snær Arnarson
# 06 Janúar 2020
# Æfingarverkefni 1

# Poem Mixer

def word_length():
    word_list = stringInput.split()
    length = len(word_list)

    # teljari = 0
    # if length != teljari:
    for i in range(length):
        word = word_list[i]
        if len(word) <= 3:
            word = word.lower()
        elif len(word) >= 7:
            word = word.upper()
        word_list[i] = word
    return word_list


def word_mixer(words):
    new_words = []
    words.sort()
    while len(words) > 5:
        new_words.append(words.pop(-5))
        new_words.append(words.pop(0))
        new_words.append(words.pop(-1))  # eða words.pop(0)
        new_words.append("\n")
    return new_words


stringInput = input("Type in string: ")

word_length()

for word in word_mixer(word_length()):
    print(word, end=" ")
