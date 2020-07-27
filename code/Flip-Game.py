class Solution(object):

    def generatePossibleNextMoves(self, s):
        a = []
        s = list(s)
        for i in range(1, len(s)):
            print '{}:{}'.format((i - 1), (i + 1))
            print s[(i - 1):(i + 1)]
            if ((s[(i - 1)] == '+') and (s[i] == '+')):
                r = list(s)
                r[(i - 1)] = '-'
                r[i] = '-'
                a.append(''.join(r))
        return a