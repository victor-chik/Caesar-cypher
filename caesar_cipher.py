def caesar(word, cipher_shift_value):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    list_word = list(word.upper())

    caeser = list_word.copy()
    for i in range(len(list_word)):
        index = alphabet.index(list_word[i])

        index = index + cipher_shift_value
        if index > (len(alphabet) - 1):
            index = index - (len(alphabet))
            caeser[i] = alphabet[index]
        else:
            caeser[i] = alphabet[index]
    return caeser
print(caesar("leonard", 2))