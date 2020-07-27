class Solution(object):

    def minEatingSpeed(self, piles, H):

        def calc(k):
            if (k == 0):
                return False
            x = [math.ceil((float(x) / float(k))) for x in piles]
            return (sum(x) <= H)
        largestValue = max(piles)
        smallestValue = 0
        found = None
        prevValue = None
        while True:
            current = (smallestValue + ((largestValue - smallestValue) / 2))
            if (current == prevValue):
                break
            x = calc(current)
            print x
            if (x == False):
                smallestValue = (current + 1)
            else:
                found = current
                largestValue = (current - 1)
            prevValue = current
        if (found != None):
            return found
        return current