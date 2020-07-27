class Leaderboard(object, ):

    def __init__(self):
        self.top10 = set()
        self.db = {}

    def addScore(self, playerId, score):
        self.db[playerId] = (self.db.get(playerId, 0) + score)

    def top(self, K):
        returnVals = []
        for (_, v) in self.db.iteritems():
            returnVals.append(v)
        g = sorted([x for x in self.db.values()], reverse=True)
        print K
        print g
        print g[:K]
        g = g[:K]
        return sum(g)

    def reset(self, playerId):
        self.db[playerId] = 0