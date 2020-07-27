class Solution(object):

    def findMin(self, nums):
        minVal = float('inf')
        for val in list(set(nums)):
            if (val < minVal):
                minVal = val
        return minVal