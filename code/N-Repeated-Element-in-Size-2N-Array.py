class Solution:

    def repeatedNTimes(self, A):
        A = sorted(A)
        for (i, val) in enumerate(A):
            if (A[i] == A[(i + 1)]):
                return A[i]