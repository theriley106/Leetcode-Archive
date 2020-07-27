class Solution(object):

    def lexicalOrder(self, n):
        return [int(a) for a in sorted([str(n) for n in xrange(1, (n + 1))])]