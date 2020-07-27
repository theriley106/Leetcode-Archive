class Solution(object):

    def dominantIndex(self, nums):
        highest_num = max(nums)
        index = nums.index(highest_num)
        nums.remove(highest_num)
        while nums:
            if (highest_num < (nums.pop((-1)) * 2)):
                return (-1)
        return index