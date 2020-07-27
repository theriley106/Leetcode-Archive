import string


class Solution(object):

    def uniqueMorseRepresentations(self, words):
        letters = list(string.ascii_lowercase)
        morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--',
                 '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..']
        morseList = []
        for word in words:
            stringVal = ''
            for letter in word:
                stringVal += morse[letters.index(letter)]
            if (stringVal not in morseList):
                morseList.append(stringVal)
        return len(morseList)
