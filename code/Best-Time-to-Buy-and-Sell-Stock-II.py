class Solution(object):

    def maxProfit(self, prices):
        profit = 0
        for i in range(len(prices)):
            if (i != 0):
                if (prices[(i - 1)] < prices[i]):
                    profit += (prices[i] - prices[(i - 1)])
        return profit