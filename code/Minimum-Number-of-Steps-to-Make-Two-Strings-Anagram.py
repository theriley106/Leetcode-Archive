class Solution(object):

    def minSteps(self, s, t):
        v1 = {}
        v2 = {}
        for v in s:
            if (v not in v1):
                v1[v] = 0
            v1[v] += 1
        for v in t:
            if (v not in v2):
                v2[v] = 0
            v2[v] += 1
        print v1
        print v2
        count = 0
        for k in set((v1.keys() + v2.keys())):
            if (v2.get(k, 0) != v1.get(k, 0)):
                count += abs((v1.get(k, 0) - v2.get(k, 0)))
        return (count / 2)