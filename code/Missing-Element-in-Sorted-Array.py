class Solution(object):

    def missingElement(self, nums, k):
        while ((len(nums) > 1) and ((nums[1] - nums[0]) <= k)):
            k -= ((nums[1] - nums.pop(0)) - 1)
        return (nums[0] + k)