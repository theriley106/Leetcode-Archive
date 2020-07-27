class MyHashSet(object, ):

    def __init__(self):
        self.max = 1000000
        self.mySet = ['_' for i in range(self.max)]

    def add(self, key):
        self.mySet[(hash(key) % self.max)] = key

    def remove(self, key):
        self.mySet[(hash(key) % self.max)] = '_'

    def contains(self, key):
        return (self.mySet[(hash(key) % self.max)] != '_')