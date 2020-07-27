class Solution(object):

    def guessNumber(self, n):
        (lowestVal, highestVal) = (0, n)
        guessNum = (n / 2)
        tValue = 1
        while (tValue != 0):
            tValue = guess(guessNum)
            if (tValue > 0):
                lowestVal = (guessNum + 1)
            if (tValue < 0):
                highestVal = (guessNum - 1)
            guessNum = ((lowestVal + highestVal) / 2)
        return guessNum