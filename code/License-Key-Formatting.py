class Solution(object):

    def licenseKeyFormatting(self, S, K):
        newS = ''
        vals = list(S.replace('-', ''))[::(-1)]
        for val in range(0, len(vals), K):
            if (val != 0):
                newS = ('-' + newS)
            for i in range(K):
                if (len(vals) == 0):
                    return newS
                newS = (str(vals.pop(0)).upper() + newS)
        return newS