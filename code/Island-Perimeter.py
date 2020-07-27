class Solution(object):

    def islandPerimeter(self, grid):

        def get_values(rowIndex, columnIndex):
            if ((rowIndex < 0) or (columnIndex < 0)):
                return 1
            if ((rowIndex >= len(grid)) or (columnIndex >= len(grid[0]))):
                return 1
            if (grid[rowIndex][columnIndex] < 1):
                return 1
            return 0

        def calc_values(rowIndex, columnIndex, count=0, back=False):
            x = 0
            x += get_values((rowIndex + 1), columnIndex)
            x += get_values((rowIndex - 1), columnIndex)
            x += get_values(rowIndex, (columnIndex + 1))
            x += get_values(rowIndex, (columnIndex - 1))
            return x
        count = 0
        for i in range(len(grid)):
            for e in range(len(grid[0])):
                if (grid[i][e] == 1):
                    count += calc_values(i, e)
        print count
        return count