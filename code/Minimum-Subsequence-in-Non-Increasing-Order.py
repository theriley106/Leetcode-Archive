class Solution(object):

    def minSubsequence(self, nums):
        x = sorted(nums)
        xSum = sum(x)
        ySum = 0
        e = []
        while (ySum <= xSum):
            t = x.pop((-1))
            xSum = (xSum - t)
            ySum += t
            e.append(t)
        return e