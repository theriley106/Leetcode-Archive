class Solution(object):

    def maxSubArray(self, nums):
        for e in range((len(nums) - 1)):
            i = (e + 1)
            if (nums[(i - 1)] > 0):
                nums[i] += nums[(i - 1)]
        return max(nums)