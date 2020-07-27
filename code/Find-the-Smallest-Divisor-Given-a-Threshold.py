import math


class Solution(object):

    def smallestDivisor(self, nums, threshold):

        def calc_for_num(i):
            r = [math.ceil((float(x) / float(i))) for x in nums]
            return sum(r)
        largestPossible = max(nums)
        smallestPossible = 0
        i = 0
        found = None
        prevCurrent = None
        while (largestPossible > smallestPossible):
            current = (smallestPossible +
                       ((largestPossible - smallestPossible) / 2))
            if ((prevCurrent == current) or (current == 0)):
                break
            x = calc_for_num(current)
            if (x <= threshold):
                found = current
                largestPossible = current
            elif (x > threshold):
                smallestPossible = current
            prevCurrent = current
        if (found != None):
            return found
        return current
