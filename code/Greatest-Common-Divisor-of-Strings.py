class Solution(object):

    def gcdOfStrings(self, str1, str2):

        def divide(stringToRemove, s):
            if (len(stringToRemove) == 0):
                return None
            if (stringToRemove in s):
                return divide(stringToRemove, s.replace(stringToRemove, '', 1))
            else:
                return s
        f = False
        vals = []
        for i in range(1, (len(str2) + 1)):
            a = (len(divide(str2[:i], str2)) == 0)
            b = (len(divide(str2[:i], str1)) == 0)
            if ((a and b) == True):
                vals.append(str2[:i])
                pass
            elif (a and (b == True) and (f == False)):
                if (i == len(str2)):
                    vals.append(str2[:i])
                f = True
        if (len(vals) == 0):
            return ''
        return vals[(-1)]