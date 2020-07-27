class Solution(object):

    def singleNonDuplicate(self, nums):
        prevVal = nums[0]
        for i in range(0, (len(nums) - 1), 2):
            print nums[i]
            print nums[(i + 1)]
            if (nums[i] != nums[(i + 1)]):
                return nums[i]
        return nums[(-1)]