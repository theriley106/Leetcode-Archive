class CustomStack(object, ):

    def __init__(self, maxSize):
        self.stack = []
        self.maxSize = maxSize

    def push(self, x):
        if (len(self.stack) < self.maxSize):
            self.stack.append(x)

    def pop(self):
        if (len(self.stack) == 0):
            return (-1)
        return self.stack.pop((-1))

    def increment(self, k, val):
        for i in range(min(len(self.stack), k)):
            self.stack[i] += val