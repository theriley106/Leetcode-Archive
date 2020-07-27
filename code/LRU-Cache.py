class LRUCache(object, ):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []
        self.dictVal = {}

    def get(self, key):
        if (key not in self.cache):
            return (-1)
        self.cache.remove(key)
        self.cache.append(key)
        return self.dictVal[str(key)]

    def put(self, key, value):
        if (key in self.cache):
            self.cache.remove(key)
        if (len(self.cache) == self.capacity):
            self.cache.pop(0)
        self.cache.append(key)
        self.dictVal[str(key)] = value