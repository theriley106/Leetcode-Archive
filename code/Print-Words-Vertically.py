class Solution(object):

    def printVertically(self, s):
        words = s.split(' ')
        maxSize = max([len(x) for x in words])
        row = [[' ' for x in range(len(words))] for i in range(maxSize)]
        for (i, word) in enumerate(words):
            for (e, letter) in enumerate(word):
                row[e][i] = letter
        a = []
        for (i, val) in enumerate(row):
            while ((len(val) > 0) and (val[(-1)] == ' ')):
                val.pop((-1))
            a.append(''.join(val))
        return a