import string


class Solution(object):

    def numSmallerByFrequency(self, queries, words):
        values = string.ascii_lowercase
        db = {}
        for (i, v) in enumerate(values):
            db[v] = i

        def f(s):
            minIndex = float('inf')
            minVal = None
            for val in s:
                if (db[val] < minIndex):
                    minIndex = db[val]
                    minVal = val
            count = 0
            for val in s:
                if (val == minVal):
                    count += 1
            return count
        for i in range(len(words)):
            words[i] = f(words[i])
        newQuery = []
        for (i, w) in enumerate(queries):
            value = f(w)
            count = 0
            for r in words:
                if (value < r):
                    count += 1
            queries[i] = count
        return queries
