class Solution(object):

    def findDuplicates(self, nums):
        a = {}
        for val in nums:
            if (val not in a):
                a[val] = 0
            a[val] += 1
        return [x for (x, y) in a.iteritems() if (y > 1)]