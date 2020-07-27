class Solution:

    def replaceWords(self, dictV, sentence):
        sentenceList = sentence.split()
        dictV.sort(key=len)
        for (i, word) in enumerate(sentenceList):
            for val in dictV:
                if (word[:len(val)] == val):
                    sentenceList[i] = val
                    break
        return ' '.join(sentenceList)