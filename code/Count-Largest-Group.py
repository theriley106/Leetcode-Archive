class Solution(object):

    def countLargestGroup(self, n):
        a = {}
        for i in range(1, (n + 1)):
            t = sum([int(x) for x in list(str(i))])
            if (t not in a):
                a[t] = []
            a[t].append(i)
        b = {}
        r = [len(x) for (k, x) in a.iteritems()]
        for v in r:
            if (v not in b):
                b[v] = 0
            b[v] += 1
        return b[max(r)]
        max()
        print a