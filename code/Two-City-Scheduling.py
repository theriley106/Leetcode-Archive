import itertools


class Solution(object):

    def twoCitySchedCost(self, costs):
        a = [(i, (c[0] - c[1])) for (i, c) in enumerate(costs)]
        result = 0
        x = sorted(a, key=(lambda k: k[1]))
        for i in range((len(costs) / 2)):
            val = x.pop(0)
            result += costs[val[0]][0]
            val = x.pop((-1))
            result += costs[val[0]][1]
        return result
