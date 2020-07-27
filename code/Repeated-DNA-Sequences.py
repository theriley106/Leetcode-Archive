class Solution(object):

    def findRepeatedDnaSequences(self, s):
        a = {}
        dup = []
        for i in range((len(s) - 9)):
            x = s[i:(i + 10)]
            if (x not in a):
                a[x] = 0
            a[x] += 1
        return [i for (i, k) in a.items() if (k > 1)]