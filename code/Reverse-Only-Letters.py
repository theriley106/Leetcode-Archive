import re


class Solution(object):

    def reverseOnlyLetters(self, S):
        letters = re.findall('[A-Za-z]', S)
        S = list(S)
        fVal = []
        for (i, val) in enumerate(S):
            if (val in letters):
                fVal.append(val)
                S[i] = None
        for (i, val) in enumerate(S):
            if (val == None):
                S[i] = fVal.pop((-1))
        return ''.join(S)
