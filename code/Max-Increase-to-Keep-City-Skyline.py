class Solution(object):

    def calc_top(self, grid):
        skyline = []
        for val in range(len(grid[0])):
            maxVal = 0
            for i in range(len(grid)):
                if (grid[i][val] > maxVal):
                    maxVal = grid[i][val]
            skyline.append(maxVal)
        return skyline

    def calc_left(self, grid):
        skyline = []
        for row in grid:
            skyline.append(max(row))
        return skyline

    def maxIncreaseKeepingSkyline(self, grid):
        b = self.calc_top(grid)
        a = self.calc_left(grid)
        toAdd = 0
        for (i, val) in enumerate(grid):
            for e in range(len(grid[0])):
                toAdd += (min(a[e], b[i]) - grid[i][e])
        return toAdd