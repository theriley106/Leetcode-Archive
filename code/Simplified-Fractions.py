class Solution(object):

    def simplifiedFractions(self, n):

        def solve_as_string(top, bottom):
            r = (float(top) / float(bottom))
            return str(r)
        if (n == 1):
            return []
        allVals = []
        vals = set()
        tVals = []
        while (n >= 2):
            for i in range(1, n):
                tVals.append([i, n])
            n = (n - 1)
        tVals.sort()
        for (i, n) in tVals:
            r = solve_as_string(i, n)
            if (r not in vals):
                vals.add(r)
                allVals.append('{}/{}'.format(i, n))
        return sorted(allVals)