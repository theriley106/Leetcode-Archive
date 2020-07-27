class Solution(object):

    def kthSmallest(self, matrix, k):

        def extract(matrix):
            a = []
            for val in matrix:
                for v in val:
                    a.append(v)
            return sorted(a)
        e = extract(matrix)
        return e[(k - 1)]