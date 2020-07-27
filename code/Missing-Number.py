class Solution(object):

    def missingNumber(self, nums):
        nums.sort()
        missingNum = list((set(range(nums[(-1)])) - set(nums)))
        if (len(missingNum) == 0):
            missingNum = (nums[(-1)] + 1)
        else:
            missingNum = missingNum[0]
        return missingNum