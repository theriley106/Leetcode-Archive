class Solution(object):

    def singleNumber(self, nums):
        a = {}
        b = set(nums)
        for val in nums:
            if (val not in a):
                a[val] = 0
            a[val] += 1
            if (a[val] == 2):
                b.remove(val)
        return list(b)[0]