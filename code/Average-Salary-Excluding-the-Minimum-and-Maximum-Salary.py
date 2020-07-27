class Solution(object):

    def average(self, salary):
        minVal = float('inf')
        maxVal = float('-inf')
        total = 0
        for v in salary:
            if (v < minVal):
                minVal = v
            if (v > maxVal):
                maxVal = v
            total += v
        print minVal
        print maxVal
        return (float(((total - minVal) - maxVal)) / (len(salary) - 2))