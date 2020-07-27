class Solution(object):

    def sortColors(self, nums):
        a = list(nums)
        while (len(nums) > 0):
            nums.pop(0)
        for val in [0, 1, 2]:
            while (val in a):
                a.remove(val)
                nums.append(val)