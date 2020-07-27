class Solution(object):

    def findPairs(self, nums, k):
        db = {}
        count = 0
        repeatVals = set()

        def try_All(index, k):
            (k - index)
            (index - k)
        if (k < 0):
            return 0
        pairs = {}
        db_counts = {}
        for val in nums:
            if (val not in db_counts):
                db_counts[val] = 0
            db_counts[val] += 1
            if (((val - k) in db) or ((k + val) in db)):
                keep = True
                temp_pairs = []
                if ((k + val) in db):
                    values = [(k + val), val]
                    pair = '_'.join([str(x) for x in sorted(values)])
                    print 'FOUND PAIR: {}, {}'.format((k + val), val)
                    temp_pairs.append(pair)
                if ((val - k) in db):
                    values = [(val - k), val]
                    pair = '_'.join([str(x) for x in sorted(values)])
                    print 'FOUND PAIR: {}, {}'.format((val - k), val)
                    temp_pairs.append(pair)
                for pair in temp_pairs:
                    if (pair not in pairs):
                        count += 1
                        pairs[pair] = 1
            db[val] = []
        print db
        print pairs
        return count
        return len(a)