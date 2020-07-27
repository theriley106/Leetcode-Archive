class Solution(object):

    def backspaceCompare(self, S, T):
        newS = []
        newT = []
        for val in S:
            if (val == '#'):
                if (len(newS) > 0):
                    newS.pop()
            else:
                newS.append(val)
        for val in T:
            if (val == '#'):
                if (len(newT) > 0):
                    newT.pop()
            else:
                newT.append(val)
        return (''.join(newS) == ''.join(newT))