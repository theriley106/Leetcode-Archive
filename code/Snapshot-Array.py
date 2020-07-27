class SnapshotArray(object, ):

    def __init__(self, length):
        self.array = [0 for i in range(length)]
        self.db = {0: {i: 0 for i in range(length)}}
        self.snapCount = 1

    def set(self, index, val):
        if ((self.snapCount - 1) not in self.db):
            self.db[(self.snapCount - 1)] = {}
        self.db[(self.snapCount - 1)][index] = val

    def snap(self):
        self.db[self.snapCount] = {}
        self.snapCount += 1
        return (self.snapCount - 2)

    def get(self, index, snap_id):
        current = snap_id
        while (index not in self.db[current]):
            current = (current - 1)
        return self.db[current][index]