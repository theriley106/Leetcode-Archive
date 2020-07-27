class RecentCounter:

    def __init__(self):
        self.listOfTime = []

    def ping(self, t):
        self.listOfTime = (
            [x for x in self.listOfTime if ((t - x) <= 3000)] + [t])
        return len(self.listOfTime)
