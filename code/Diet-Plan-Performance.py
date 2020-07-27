class Solution(object):

    def dietPlanPerformance(self, calories, k, lower, upper):
        finalTotal = 0
        sumVal = sum(calories[0:(0 + k)])
        prevVal = None
        for e in xrange(((len(calories) - k) + 1)):
            if (e == 0):
                pass
            else:
                sumVal = ((sumVal - prevVal) + calories[((e + k) - 1)])
            total = sumVal
            prevVal = calories[e]
            if (total < lower):
                finalTotal -= 1
            if (total > upper):
                finalTotal += 1
        return finalTotal