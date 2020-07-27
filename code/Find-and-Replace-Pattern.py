class Solution(object):

    def findAndReplacePattern(self, words, pattern):
        goodWords = []
        for word in words:
            tempInfo = {}
            cont = True
            if (len(pattern) != len(word)):
                contVal = False
            else:
                for (i, beat) in enumerate(pattern):
                    letter = word[i]
                    if (beat in tempInfo):
                        if (letter != tempInfo[beat]):
                            cont = False
                            break
                    else:
                        tempInfo[beat] = letter
            print tempInfo
            if ((cont == True) and (len(set(tempInfo.values())) == len(tempInfo.keys()))):
                goodWords.append(word)
        return goodWords