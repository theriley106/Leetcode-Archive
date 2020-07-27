class MyStack(object, ):

    def __init__(self):
        self.q = []

    def push(self, x):
        self.q.append(x)

    def pop(self):
        a = self.q[(-1)]
        del self.q[(-1)]
        return a

    def top(self):
        return self.q[(-1)]

    def empty(self):
        return (len(self.q) == 0)