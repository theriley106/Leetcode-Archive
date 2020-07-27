class Solution(object):

    def kWeakestRows(self, mat, k):

        def get_length(row):
            count = 0
            while ((len(row) > 0) and (row[0] == 1)):
                row.pop(0)
                count += 1
            return count
        a = []
        for (i, row) in enumerate(mat):
            a.append([i, get_length(row)])
        a.sort(key=(lambda k: k[1]))
        return [a[i][0] for i in range(k)]