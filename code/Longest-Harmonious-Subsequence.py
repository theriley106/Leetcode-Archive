class Solution(object):

    def findLHS(self, nums):
        a = {}
        for val in nums:
            if (val not in a):
                a[val] = 0
            a[val] += 1
        v = 0
        g = sorted(a.keys())
        j = []
        for i in range(0, (len(g) - 1)):
            if (abs((g[(i + 1)] - g[i])) < 2):
                j.append(sum([a[g[i]], a[g[(i + 1)]]]))
        if (len(j) > 0):
            return max(j)
        return 0