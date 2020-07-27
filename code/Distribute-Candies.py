class Solution(object):

    def distributeCandies(self, candies):
        if (len(list(set(candies))) > (len(candies) / 2)):
            return (len(candies) / 2)
        else:
            return len(list(set(candies)))