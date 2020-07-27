import itertools


class Solution(object):

    def numTilePossibilities(self, tiles):
        a = 0
        for e in range(1, (len(tiles) + 1)):
            for val in set(itertools.permutations(tiles, e)):
                a += 1
        return a
