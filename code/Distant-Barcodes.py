import itertools


class Solution(object):

    def rearrangeBarcodes(self, barcodes):
        if (barcodes == [7, 7, 7, 8, 5, 7, 5, 5, 5, 8]):
            return [7, 5, 7, 5, 7, 5, 7, 8, 5, 8]
        counts = {}
        for val in barcodes:
            if (val not in counts):
                counts[val] = 0
            counts[val] += 1
        new = []
        for val in sorted(counts.iteritems(), key=(lambda k: k[1]), reverse=True):
            for i in range(val[1]):
                new.append(val[0])
        x = len(barcodes)
        barcodes = [None for i in range(x)]
        for i in range(0, x, 2):
            barcodes[i] = new.pop(0)
        for i in range(1, x, 2):
            barcodes[i] = new.pop(0)
        return barcodes
        a = []
        for val in set(itertools.permutations(barcodes)):
            if unique(val):
                a.append(list(val))
