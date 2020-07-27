class Solution(object):

    def maxProfit(self, prices):
        maxProfit = 0
        if (len(prices) > 0):
            minPrice = prices[0]
        for i in xrange(len(prices)):
            if (prices[i] < minPrice):
                minPrice = prices[i]
            if ((prices[i] - minPrice) > maxProfit):
                maxProfit = (prices[i] - minPrice)
        return maxProfit