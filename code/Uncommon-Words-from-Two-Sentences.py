class Solution(object):

    def uncommonFromSentences(self, A, B):
        A = A.split(' ')
        B = B.split(' ')
        BOTH = (A + B)
        listOfVals = []
        for val in set(BOTH):
            if (BOTH.count(val) == 1):
                listOfVals.append(val)
        return listOfVals