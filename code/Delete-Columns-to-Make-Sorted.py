import string


class Solution(object):

    def minDeletionSize(self, A):
        alphabet = list(string.ascii_lowercase)
        db = {}
        for (i, val) in enumerate(alphabet):
            db[val] = i
        maxLength = max([len(x) for x in A])
        a = []
        for i in xrange(maxLength):
            inOrder = True
            prev = (-1)
            for e in xrange(len(A)):
                if (len(A[e]) > i):
                    if (prev > db.get(A[e][i])):
                        inOrder = False
                    prev = db.get(A[e][i])
            if (inOrder == False):
                a.append(i)
        print a
        return len(a)
