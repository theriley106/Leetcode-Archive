class Solution(object):

    def sortString(self, s):
        self.db = {}
        for val in s:
            if (val not in self.db):
                self.db[val] = 0
            self.db[val] += 1
        self.vals = sorted(self.db.keys())
        self.vals2 = sorted(self.db.keys(), reverse=True)
        result = ''
        while (len(self.db.keys()) > 0):
            for v in sorted(self.db.keys()):
                if (self.db[v] > 0):
                    self.db[v] = (self.db[v] - 1)
                    result += v
                    if (self.db[v] == 0):
                        del self.db[v]
            for v in sorted(self.db.keys(), reverse=True):
                if (self.db[v] > 0):
                    self.db[v] = (self.db[v] - 1)
                    result += v
                    if (self.db[v] == 0):
                        del self.db[v]
        return result