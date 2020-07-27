class Solution(object):

    def smallestEquivalentString(self, A, B, S):
        db = {}
        prev = set()

        def get_e(letter, prev=None):
            if (prev == None):
                prev = set()
            if (letter in prev):
                return []
            if (letter not in db):
                return [letter]
            r = list(db[letter])
            prev.add(letter)
            for v in db[letter]:
                for x in get_e(v, prev):
                    r.append(x)
            return r
        for i in range(len(A)):
            if (A[i] != B[i]):
                if (A[i] not in db):
                    db[A[i]] = set()
                if (B[i] not in db):
                    db[B[i]] = set()
                db[A[i]].add(B[i])
                db[B[i]].add(A[i])
        newDB = {}
        for (k, v) in db.iteritems():
            newDB[k] = set()
            for val in v:
                temp = get_e(val)
                print temp
                for t in temp:
                    newDB[k].add(t)

        def get_all_combinations(word, prev=[]):
            allVals = []
            if (len(word) == 0):
                return prev
            letter = word.pop(0)
            for val in get_e(letter):
                for word in prev:
                    word += val
        a = ''
        for val in S:
            x = sorted(list(get_e(val)))
            a += x[0]
        return a