class Solution(object):

    def canJump(self, nums):
        a = ['U' for i in range(len(nums))]
        lastIndex = (len(nums) - 1)
        startIndex = (lastIndex - 1)
        while (startIndex >= 0):
            if ((nums[startIndex] + startIndex) >= lastIndex):
                lastIndex = startIndex
            startIndex -= 1
        return (lastIndex == 0)
        print startIndex