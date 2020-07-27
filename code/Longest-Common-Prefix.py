class Solution(object):

    def longestCommonPrefix(self, strs):
        keep = True
        stringVal = ''
        a = 0
        while (keep == True):
            val = ''
            for val in strs:
                if (len(val) > a):
                    if (val[a] != strs[0][a]):
                        keep = False
                        break
                else:
                    break
            if ((keep == True) and (len(val) > a)):
                stringVal += str(val[a])
                a += 1
            else:
                break
        return stringVal