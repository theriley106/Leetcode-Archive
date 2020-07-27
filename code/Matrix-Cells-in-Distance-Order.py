class Solution(object):

    def allCellsDistOrder(self, R, C, r0, c0):
        final = []
        for i in range(R):
            for e in range(C):
                column = [i, e]
                final.append(
                    {'distance': (abs((column[0] - r0)) + abs((column[1] - c0))), 'co': column})
        return [k['co'] for k in sorted(final, key=(lambda k: k['distance']))]
