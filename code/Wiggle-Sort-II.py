class Solution(object):

    def wiggleSort(self, nums):
        g = sorted(nums, reverse=True)
        x = len(nums)
        while (len(nums) > 0):
            nums.pop(0)
        for i in range(x):
            nums.append(None)
        for i in range(1, len(nums), 2):
            nums[i] = g.pop(0)
        for i in range(len(nums)):
            if (nums[i] == None):
                nums[i] = g.pop(0)