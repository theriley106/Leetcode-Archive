class Solution(object):

    def arrayRankTransform(self, arr):
        db = {}
        for (i, v) in enumerate(sorted(list(set(arr)))):
            rank = (i + 1)
            db[v] = rank
        for (i, val) in enumerate(arr):
            arr[i] = db[val]
        return arr