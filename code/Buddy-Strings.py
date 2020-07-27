class Solution(object):

    def buddyStrings(self, A, B):
        diff = []
        if (abs((len(A) - len(B))) > 0):
            print 'NAH'
            return False
        if (len(A) < 2):
            return False
        A = list(A)
        B = list(B)
        for i in range(len(A)):
            if (A[i] != B[i]):
                if (len(diff) > 0):
                    g = diff.pop(0)
                    A[g[1]] = A[i]
                    A[i] = g[0]
                    print ''.join(A)
                    print ''.join(B)
                    return (''.join(A) == ''.join(B))
                diff.append([A[i], i])
        if ((''.join(A) == ''.join(B)) and (len(set((A + B))) != 1)):
            db = {}
            for val in A:
                if (val not in db):
                    db[val] = True
                else:
                    return True
            return False
        return (len(diff) == 0)