class Solution:

    def singleNumber(self, nums):
        return [x for x in set(nums) if (nums.count(x) == 1)][0]