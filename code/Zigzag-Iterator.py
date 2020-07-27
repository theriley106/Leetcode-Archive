class ZigzagIterator(object, ):

    def __init__(self, v1, v2):
        self.vals = [v1, v2]
        self.last = False

    def reset(self):
        if (len(self.vals[(-1)]) == 0):
            self.vals.pop((-1))
        if ((len(self.vals) > 0) and (len(self.vals[0]) == 0)):
            self.vals.pop(0)
        return (len(self.vals) != 0)

    def next(self):
        self.reset()
        if ((len(self.vals) == 2) and (self.last == True)):
            self.last = (not self.last)
            return self.vals[1].pop(0)
        else:
            self.last = (not self.last)
            return self.vals[0].pop(0)

    def hasNext(self):
        return self.reset()