class Solution(object):

    def firstMissingPositive(self, nums):
        if (len(nums) > 0):
            minVal = min(nums)
            maxVal = max(nums)
            for v in xrange(1, (maxVal + 2)):
                if (v not in nums):
                    return v
                else:
                    print v
        return 1