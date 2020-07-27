class Solution(object):

    def firstUniqChar(self, s):
        listOfVals = []
        a = {}
        for val in s:
            if (val not in a):
                a[val] = 0
            a[val] += 1
        for (i, val) in enumerate(list(s)):
            if (a[val] == 1):
                return i
        return (-1)