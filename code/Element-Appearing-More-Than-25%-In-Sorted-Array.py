class Solution(object):

    def findSpecialInteger(self, arr):
        a = {}
        maxLength = (len(arr) / 4)
        for val in arr:
            if (val not in a):
                a[val] = 0
            a[val] += 1
            if (a[val] > maxLength):
                return val