import re


class Solution(object):

    def shortestCompletingWord(self, licensePlate, words):
        letters = ''.join([x.lower() for x in re.findall(
            'D', licensePlate.replace(' ', ''))])
        print letters
        lowestWord = None
        lowestCount = None
        for word in words:
            similar = 10
            ogWord = word
            f = len(word)
            contVal = True
            for val in letters:
                if (val not in word):
                    contVal = False
                word = word.replace(val, '', 1)
            if (contVal == True):
                if (lowestCount == None):
                    lowestCount = f
                    lowestWord = ogWord
                elif (lowestCount > f):
                    lowestCount = f
                    lowestWord = ogWord
        return lowestWord
