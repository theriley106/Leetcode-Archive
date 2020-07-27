class Solution(object):

    def longestPalindrome(self, s):
        a = {}
        for t in s:
            if (t not in a):
                a[t] = 0
            a[t] += 1
        g = {}
        d = sorted(a.values(), reverse=True)
        count = 0
        used = []
        print d
        for val in d:
            if ((val % 2) == 0):
                count += val
                used.append(val)
        for v in used:
            d.remove(v)
        if (len(d) > 0):
            count += 1
        print d
        for val in d:
            count += (val - 1)
        return count