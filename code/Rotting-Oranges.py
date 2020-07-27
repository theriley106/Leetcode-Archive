class Solution(object):

    def mark_all(self, rowIndex, columnIndex):
        count = 0
        changed = []
        if (self.grid[rowIndex][columnIndex] == 2):
            if (rowIndex != (len(self.grid) - 1)):
                if (self.grid[(rowIndex + 1)][columnIndex] == 1):
                    count += 1
                    self.grid[(rowIndex + 1)][columnIndex] += 1
                    changed.append(((rowIndex + 1), columnIndex))
            if (rowIndex != 0):
                if (self.grid[(rowIndex - 1)][columnIndex] == 1):
                    count += 1
                    self.grid[(rowIndex - 1)][columnIndex] += 1
                    changed.append(((rowIndex - 1), columnIndex))
            if (columnIndex != (len(self.grid[0]) - 1)):
                if (self.grid[rowIndex][(columnIndex + 1)] == 1):
                    count += 1
                    self.grid[rowIndex][(columnIndex + 1)] += 1
                    changed.append((rowIndex, (columnIndex + 1)))
            if (columnIndex != 0):
                if (self.grid[rowIndex][(columnIndex - 1)] == 1):
                    count += 1
                    self.grid[rowIndex][(columnIndex - 1)] += 1
                    changed.append((rowIndex, (columnIndex - 1)))
        return (count, changed)

    def orangesRotting(self, grid):
        self.grid = grid
        minutes = 0
        while True:
            count = 0
            minutes += 1
            changed = []
            for (i, row) in enumerate(grid):
                for (e, column) in enumerate(row):
                    if ((i, e) not in changed):
                        (t, c) = self.mark_all(i, e)
                        count += t
                        changed += c
            if (count == 0):
                break
        return ((minutes - 1) if (len([x for x in [g for g in grid] if (1 in x)]) == 0) else (-1))