class ProductOfNumbers(object, ):

    def __init__(self):
        self.vals = []
        self.prev = {}

    def add(self, num):
        self.vals.append(num)
        keys = self.prev.keys()
        for k in keys:
            del self.prev[k]

    def getProduct(self, k):
        if (k in self.prev):
            return self.prev[k]
        v = 1
        k = min(k, len(self.vals))
        for val in self.vals[(- k):]:
            v *= val
        self.prev[k] = v
        return v