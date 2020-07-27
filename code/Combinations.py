import itertools


class Solution(object):

    def combine(self, n, k):
        return list(itertools.combinations(list(range(1, (n + 1))), k))
