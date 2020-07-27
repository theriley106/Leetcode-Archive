class MyCircularQueue(object, ):

    def __init__(self, k):
        self.arrayVal = []
        minVal = (k - 1)
        self.k = k

    def enQueue(self, value):
        while (len(self.arrayVal) == self.k):
            return False
        self.arrayVal.append(value)
        return True

    def deQueue(self):
        if (len(self.arrayVal) == 0):
            return False
        self.arrayVal.pop(0)
        return True

    def Front(self):
        try:
            return self.arrayVal[0]
            return self.arrayVal.pop(0)
        except:
            return (-1)

    def Rear(self):
        try:
            return self.arrayVal[(-1)]
            return self.arrayVal.pop((-1))
        except:
            return (-1)

    def isEmpty(self):
        return (len(self.arrayVal) == 0)

    def isFull(self):
        print self.arrayVal
        return (len(self.arrayVal) == self.k)