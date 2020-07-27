class Solution(object):

    def moveZeroes(self, nums):
        totalZero = nums.count(0)
        if (totalZero != len(nums)):
            print totalZero
            newList = []
            while (0 in nums):
                nums.remove(0)
            for var in range(totalZero):
                nums.append(0)