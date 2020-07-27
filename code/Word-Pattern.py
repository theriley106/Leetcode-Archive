class Solution(object):

    def wordPattern(self, pattern, stringVal):
        tempo = {}
        stringList = stringVal.split(' ')
        print pattern
        print stringVal
        if (len(pattern) != len(stringList)):
            return False
        for i in range(len(pattern)):
            tempoVal = pattern[i]
            string = stringList[i]
            if (tempoVal in tempo):
                if (tempo[tempoVal] != string):
                    return False
            else:
                if (string in tempo.values()):
                    return False
                tempo[tempoVal] = string
        return True