class Solution(object):

    def shiftGrid(self, grid, k):
        row = len(grid)
        column = len(grid[0])
        r = []
        tempGrid = [['' for i in range(column)] for e in range(row)]
        while (len(grid) > 0):
            x = grid.pop(0)
            while (len(x) > 0):
                r.append(x.pop(0))
        print r
        for i in range(k):
            r.insert(0, r.pop((-1)))
        for i in range(len(tempGrid)):
            for e in range(len(tempGrid[0])):
                tempGrid[i][e] = r.pop(0)
        return tempGrid
        print r