class Solution(object):

    def numberOfDays(self, Y, M):
        thirtyOne = [1, 3, 4, 7, 8, 10, 12]
        thirty = [4, 6, 9, 11]
        if (((Y % 4) == 0) and (M == 2)):
            if ((Y % 100) == 0):
                if ((Y % 400) == 0):
                    return 29
                else:
                    return 28
            return 29
        elif (((Y % 4) != 0) and (M == 2)):
            return 28
        elif (M in thirty):
            return 30
        else:
            return 31