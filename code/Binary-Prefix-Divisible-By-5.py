class Solution(object):

    def prefixesDivBy5(self, A):
        r = []
        A = ''.join([str(x) for x in A])
        for i in xrange(1, (len(A) + 1)):
            r.append(((int(A[0:i], 2) % 5) == 0))
        return r