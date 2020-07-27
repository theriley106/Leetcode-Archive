class Solution(object):

    def getClosest(self, index, listOfIndex):
        closest = 999999999
        bestIndex = 0
        for val in listOfIndex:
            if (abs((index - val)) < closest):
                closest = abs((index - val))
                bestIndex = val
        return closest

    def shortestToChar(self, S, C):
        tempS = list(S)
        indexes = []
        newValz = []
        count = 0
        while (C in tempS):
            datIndex = tempS.index(C)
            indexes.append((datIndex + count))
            tempS.pop(datIndex)
            count += 1
        for (i, val) in enumerate(S):
            newValz.append(self.getClosest(i, indexes))
        return newValz