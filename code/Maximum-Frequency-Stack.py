class FreqStack(object, ):

    def __init__(self):
        self.db = {}
        self.priorityQ = []

    def insert(self, value):
        return

    def remove(self, value):
        return

    def push(self, x):
        if (x not in self.db):
            self.db[x] = 0
        self.db[x] += 1
        value = (x, self.db[x])
        i = 0
        while (i < len(self.priorityQ)):
            if (self.priorityQ[i][0] < self.db[x]):
                pass
            else:
                break
            i += 1
        if (i == len(self.priorityQ)):
            self.priorityQ.append((self.db[x], [x]))
        else:
            self.priorityQ[i][1].append(x)

    def pop(self):
        r = self.priorityQ[(-1)][1].pop((-1))
        if (len(self.priorityQ[(-1)][1]) == 0):
            self.priorityQ.pop((-1))
        self.db[r] -= 1
        return r