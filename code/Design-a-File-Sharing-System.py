class FileSharing(object, ):

    def __init__(self, m):
        self.chunks = m
        self.lowestId = 1
        self.db = {}
        for i in range(1, (m + 1)):
            self.db[i] = set()
        self.leftOverIds = []

    def join(self, ownedChunks):
        print self.leftOverIds
        if (len(self.leftOverIds) == 0):
            x = self.lowestId
        else:
            x = self.leftOverIds.pop(0)
            self.lowestId -= 1
        for v in ownedChunks:
            self.db[v].add(x)
        self.lowestId += 1
        return x

    def leave(self, userID):
        for (k, v) in self.db.iteritems():
            if (userID in v):
                v.remove(userID)
        self.leftOverIds.append(userID)
        self.leftOverIds.sort()

    def request(self, userID, chunkID):
        vals = sorted(list(self.db[chunkID]))
        if (len(vals) > 0):
            self.db[chunkID].add(userID)
        return vals