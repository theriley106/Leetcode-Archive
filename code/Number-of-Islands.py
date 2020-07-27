class Solution(object):

    def is_island(self, rowIndex, columnIndex):
        return (int(self.grid[rowIndex][columnIndex]) > 0)

    def dfs(self, rowIndex, columnIndex):
        if ((rowIndex < 0) or (rowIndex >= self.rows)):
            return
        if ((columnIndex < 0) or (columnIndex >= self.columns)):
            return
        if (self.is_island(rowIndex, columnIndex) == False):
            return
        self.grid[rowIndex][columnIndex] = (-1)
        self.dfs((rowIndex + 1), columnIndex)
        self.dfs((rowIndex - 1), columnIndex)
        self.dfs(rowIndex, (columnIndex + 1))
        self.dfs(rowIndex, (columnIndex - 1))

    def numIslands(self, grid):
        self.grid = grid
        if (len(self.grid) == 0):
            return 0
        total_islands = 0
        self.rows = len(self.grid)
        self.columns = len(self.grid[0])
        for rowIndex in range(self.rows):
            for columnIndex in range(self.columns):
                if (self.is_island(rowIndex, columnIndex) == True):
                    total_islands += 1
                    self.dfs(rowIndex, columnIndex)
        return total_islands