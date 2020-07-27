class MyQueue(object, ):

    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        a = self.stack[0]
        del self.stack[0]
        return a

    def peek(self):
        return self.stack[0]

    def empty(self):
        return (len(self.stack) == 0)