class Trie(object, ):

    def __init__(self):
        self.left = None
        self.right = None

    def insert(self, value):
        return


class Solution(object):

    def camelMatch(self, queries, pattern):
        values = []
        for e in queries:
            a = list(e)
            new = list(pattern)
            i = 0
            while ((len(a) > 0) and (len(new) > 0) and ((a[0] == new[0]) or (a[0].lower() == a[0]))):
                if (a[0] == new[0]):
                    new.pop(0)
                a.pop(0)
            print a
            print new
            r = ''.join(a)
            if ((r == r.lower()) and (len(new) == 0)):
                values.append(True)
            else:
                values.append(False)
        return values
