import string


class Solution(object):

    def freqAlphabets(self, s):
        alphabet = list(string.ascii_lowercase)
        db = {}
        for i in range(1, 10):
            db[str(i)] = alphabet.pop(0)
        db2 = {}
        for i in range(10, 27):
            db2[(str(i) + '#')] = alphabet.pop(0)
        for (k, v) in db2.iteritems():
            s = s.replace(k, v)
        for (k, v) in db.iteritems():
            s = s.replace(k, v)
        return s
