class Solution(object):

    def numSubseq(self, nums, target):
        nums = sorted(nums)
        leftVal = 0
        rightVal = (len(nums) - 1)
        count = 0
        while (leftVal <= rightVal):
            if ((nums[leftVal] + nums[rightVal]) > target):
                rightVal -= 1
            else:
                count = ((count + int((2 ** (rightVal - leftVal)))) %
                         ((10 ** 9) + 7))
                leftVal += 1
        return (count % ((10 ** 9) + 7))
