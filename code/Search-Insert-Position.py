class Solution(object):

    def searchInsert(self, nums, target):
        try:
            return nums.index(target)
        except:
            if (target > nums[(-1)]):
                return (int(nums.index(nums[(-1)])) + 1)
            if (target < nums[0]):
                return 0
            for (i, var) in enumerate(nums):
                if ((target < var) and (target > nums[(i - 1)])):
                    return i