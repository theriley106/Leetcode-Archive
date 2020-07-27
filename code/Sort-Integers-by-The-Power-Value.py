class Solution(object):

    def getKth(self, lo, hi, k):

        def power(num):
            if (num == 1):
                return 0
            if ((num % 2) == 0):
                return (1 + power((num / 2)))
            else:
                return (1 + power(((3 * num) + 1)))
        x = range(lo, (hi + 1))
        a = {}
        for val in x:
            e = power(val)
            if (e not in a):
                a[e] = []
            a[e].append(val)
        listVal = []
        keys = sorted(a.keys())
        for val in keys:
            for v in sorted(a[val]):
                listVal.append(v)
        print listVal
        return listVal[(k - 1)]