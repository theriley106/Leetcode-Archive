import itertools


class Solution(object):

    def largestPerimeter(self, A):

        def calc(tri):
            x = sum(tri)
            for i in range(3):
                if (tri[i] >= (x - tri[i])):
                    return 0
            return sum(tri)
        maxVal = 0
        A.sort()
        print A
        for i in range(len(A)):
            j = [A[((- i) - 1)], A[((- i) - 2)], A[((- i) - 3)]]
            print j
            x = calc(j)
            if (x != 0):
                return x
            if (abs(((- i) - 4)) > len(A)):
                break
        return 0
