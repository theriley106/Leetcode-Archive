class Solution(object):

    def smallerNumbersThanCurrent(self, nums):
        sortedVals = sorted(nums)
        return [sortedVals.index(x) for x in nums]