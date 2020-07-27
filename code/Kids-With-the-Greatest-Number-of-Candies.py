class Solution(object):

    def kidsWithCandies(self, candies, extraCandies):
        maxVal = 0
        a = []
        for val in candies:
            maxVal = max(maxVal, val)
        for val in candies:
            if ((val + extraCandies) >= maxVal):
                a.append(True)
            else:
                a.append(False)
        return a