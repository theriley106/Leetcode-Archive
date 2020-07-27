class Solution(object):

    def findUnsortedSubarray(self, nums):
        newVals = sorted(nums)
        start = 0
        end = len(nums)
        for (i, val) in enumerate(nums):
            if (newVals[i] != nums[i]):
                if (start == 0):
                    start = (i + 1)
                end = (i + 1)
        if (start == 0):
            return 0
        return ((end - start) + 1)