class Solution(object):

    def searchMatrix(self, matrix, target):
        for val in matrix:
            if (len(val) > 2):
                if ((val[(-1)] >= target) and (val[0] <= target)):
                    if (target in val):
                        return True
            elif (target in val):
                return True
        return False