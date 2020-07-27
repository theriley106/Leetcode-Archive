class Solution(object):

    def majorityElement(self, nums):
        lowest = 0
        for var in list(set(nums)):
            if (nums.count(var) > lowest):
                lowest = nums.count(var)
                newVar = var
        return newVar