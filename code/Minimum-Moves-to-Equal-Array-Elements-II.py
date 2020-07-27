class Solution(object):

    def minMoves2(self, nums):
        nums.sort()
        if (len(list(set(nums))) == 1):
            return 0
        median = nums[(len(nums) / 2)]
        count = 0
        for val in nums:
            count += abs((median - val))
        return count