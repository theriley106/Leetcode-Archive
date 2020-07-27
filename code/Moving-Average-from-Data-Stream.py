class MovingAverage(object, ):

    def __init__(self, size):
        self.size = size
        self.arrayVals = []

    def next(self, val):
        if (len(self.arrayVals) == self.size):
            self.arrayVals.pop(0)
        self.arrayVals.append(val)
        return (sum(self.arrayVals) / float(len(self.arrayVals)))