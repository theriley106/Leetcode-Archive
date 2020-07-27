class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        a = [[None for i in range(len(text1))] for e in range(len(text2))]
        db = {}

        def lcs(row, column):
            if ((row, column) in db):
                return db[(row, column)]
            db[(row, column)] = 0
            if ((row < 0) or (column < 0)):
                return 0
            if (text1[row] == text2[column]):
                x = (1 + lcs((row - 1), (column - 1)))
                db[(row, column)] = x
                return x
            else:
                x = max(lcs((row - 1), column), lcs(row, (column - 1)))
                db[(row, column)] = x
                return x
        return lcs((len(text1) - 1), (len(text2) - 1))