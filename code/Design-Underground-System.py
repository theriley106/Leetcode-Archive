class UndergroundSystem(object, ):

    def __init__(self):
        self.db = {}
        self.timeTables = {}

    def checkIn(self, id, stationName, t):
        self.db[id] = {'name': stationName, 'time': t}

    def checkOut(self, id, stationName, t):
        r = (stationName, self.db[id]['name'])
        if (r not in self.timeTables):
            self.timeTables[r] = []
        self.timeTables[r].append((t - self.db[id]['time']))
        r = (self.db[id]['name'], stationName)
        if (r not in self.timeTables):
            self.timeTables[r] = []
        self.timeTables[r].append((t - self.db[id]['time']))

    def getAverageTime(self, startStation, endStation):
        avg = (float(sum(self.timeTables[(startStation, endStation)])) /
               float(len(self.timeTables[(startStation, endStation)])))
        return avg
