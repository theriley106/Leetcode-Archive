import itertools


class Solution(object):

    def canThreePartsEqualSum(self, A):
        if ((sum(A) % 3) != 0):
            return False
        target = (sum(A) / 3)
        count = 0
        tempCount = 0
        for val in A:
            tempCount += val
            if (tempCount == target):
                count += 1
                tempCount = 0
        return (count == 3)
