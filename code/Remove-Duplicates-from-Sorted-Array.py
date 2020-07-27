class Solution(object):

    def removeDuplicates(self, nums):
        if (len(nums) < 2):
            return
        i = 0
        while True:
            if (nums[i] == nums[(i + 1)]):
                nums.pop((i + 1))
            else:
                i += 1
            if (i >= (len(nums) - 1)):
                break