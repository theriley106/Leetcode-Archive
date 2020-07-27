class Solution(object):

    def findMaxConsecutiveOnes(self, nums):
        total_count = 0
        isOne = False
        while (len(nums) > 0):
            num = nums.pop(0)
            tempList = 0
            if (num == 1):
                tempList += 1
            while (num == 1):
                if (len(nums) == 0):
                    break
                num = nums.pop(0)
                if (num == 1):
                    tempList += 1
            if (tempList > total_count):
                total_count = tempList
        return total_count