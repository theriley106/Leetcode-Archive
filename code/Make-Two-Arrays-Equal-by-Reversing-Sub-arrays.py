class Solution(object):

    def canBeEqual(self, target, arr):
        a = {}
        for val in target:
            if (val not in a):
                a[val] = 0
            a[val] += 1
        for val in arr:
            if (val not in a):
                return False
            a[val] -= 1
        for val in a.keys():
            if (a == 0):
                return False
        return True