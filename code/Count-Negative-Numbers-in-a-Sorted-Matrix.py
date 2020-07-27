class Solution(object):

    def countNegatives(self, grid):
        count = 0
        for v in grid:
            for g in v:
                if (g < 0):
                    count += 1
        return count