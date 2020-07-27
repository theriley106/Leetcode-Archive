class Solution(object):

    def findCheapestPrice(self, n, flights, src, dst, K):
        self.maxLength = K
        self.src = src
        self.dst = dst
        self.flightDB = {}
        self.lowestVal = float('inf')
        self.flightPath = None
        for (i, val) in enumerate(flights):
            if (val[0] not in self.flightDB):
                self.flightDB[val[0]] = []
            self.flightDB[val[0]].append(
                {'id': i, 'destination': val[1], 'cost': val[2]})
        self.finished = {}

        def getAllRoutes(start, cost, past=[], visited=[]):
            if (cost > self.lowestVal):
                return
            if (len(visited) != len(set(visited))):
                return
            if (len(past) > (self.maxLength + 1)):
                return
            if (start == self.dst):
                if (cost < self.lowestVal):
                    self.lowestVal = cost
                    self.flightPath = past
            for val in self.flightDB.get(start, []):
                if ((val['id'] not in past) and (val['destination'] not in visited)):
                    getAllRoutes(val['destination'], (cost + val['cost']),
                                 (past + [val['id']]), (visited + [start]))
        for val in self.flightDB.get(src, []):
            getAllRoutes(val['destination'], val['cost'], [val['id']], [src])
        if (self.lowestVal == float('inf')):
            return (-1)
        return self.lowestVal
