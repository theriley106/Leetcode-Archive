class MinStack(object, ):

    def __init__(self):
        self.listOfNums = []

    def push(self, x):
        self.listOfNums.append(x)

    def pop(self):
        self.listOfNums.pop()

    def top(self):
        return self.listOfNums[(-1)]

    def getMin(self):
        return min(self.listOfNums)