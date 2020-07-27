class Solution(object):

    def sumOfDigits(self, A):
        minVal = float('inf')
        for val in A:
            if (val < minVal):
                minVal = val
        sumVal = 0
        for num in str(minVal):
            sumVal += int(num)
        if ((sumVal % 2) != 0):
            return 0
        return 1