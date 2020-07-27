class Solution(object):

    def finalPrices(self, prices):
        newVals = sorted(prices)
        values = []
        for i in range(len(prices)):
            e = (i + 1)
            while ((e < len(prices)) and (prices[e] > prices[i])):
                e += 1
            try:
                discount = prices[e]
            except:
                discount = 0
            values.append((prices[i] - discount))
        return values