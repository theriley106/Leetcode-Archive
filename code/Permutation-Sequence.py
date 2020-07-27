import itertools


class Solution(object):

    def getPermutation(self, n, k):
        count = 0
        for val in itertools.permutations(list(xrange(1, (n + 1)))):
            count += 1
            if (count == k):
                break
        list_of_vals = [str(x) for x in val]
        return ''.join(list_of_vals)
