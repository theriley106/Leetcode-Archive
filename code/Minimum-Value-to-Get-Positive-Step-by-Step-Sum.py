class Solution(object):

    def minStartValue(self, nums):
        start = 1
        while True:
            currSum = start
            negative = False
            for val in nums:
                currSum += val
                if (currSum < 1):
                    negative = True
                    break
            if (negative == False):
                return start
            start += 1