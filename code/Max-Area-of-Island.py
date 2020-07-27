class Solution(object):

    def maxAreaOfIsland(self, grid):
        self.grid = grid
        maxVal = 0
        for rowIndex in range(len(grid)):
            for columnIndex in range(len(grid[0])):
                if (self.grid[rowIndex][columnIndex] > 0):
                    self.count = 0
                    tempCount = self.dfs(rowIndex, columnIndex)
                    if (self.count > maxVal):
                        maxVal = self.count
        return maxVal

    def dfs(self, rowIndex, columnIndex):
        if ((rowIndex >= len(self.grid)) or (columnIndex >= len(self.grid[0])) or (rowIndex < 0) or (columnIndex < 0)):
            return
        if (self.grid[rowIndex][columnIndex] < 1):
            return
        self.count += 1
        self.grid[rowIndex][columnIndex] = (-1)
        self.dfs(rowIndex, (columnIndex + 1))
        self.dfs(rowIndex, (columnIndex - 1))
        self.dfs((rowIndex + 1), columnIndex)
        self.dfs((rowIndex - 1), columnIndex)