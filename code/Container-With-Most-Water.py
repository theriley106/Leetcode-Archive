class Solution(object):

    def calc_water(self, index1, index2):
        try:
            minHeight = min(self.grid[index1], self.grid[index2])
            width = (index2 - index1)
            return (minHeight * width)
        except:
            return 0

    def maxArea(self, height):
        self.grid = height
        bigVal = 0
        startLeft = 0
        totalLen = len(height)
        startRight = (totalLen - 1)
        while (startLeft < startRight):
            g = self.calc_water(startLeft, startRight)
            if (g > bigVal):
                bigVal = g
            if (min(self.grid[startLeft], self.grid[startRight]) == self.grid[startLeft]):
                startLeft += 1
            else:
                startRight -= 1
        return bigVal