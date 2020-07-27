class Solution(object):

    def findLengthOfLCIS(self, nums):
        largest = 0
        prevVal = 0
        count = 0
        while (len(nums) > 0):
            thisVal = nums.pop(0)
            if (thisVal > prevVal):
                count += 1
            else:
                count = 1
            if (count > largest):
                largest = count
            prevVal = thisVal
        return largest