class Solution(object):

    def runningSum(self, nums):
        currentVal = 0
        for i in range(len(nums)):
            nums[i] = (nums[i] + currentVal)
            currentVal = nums[i]
        return nums