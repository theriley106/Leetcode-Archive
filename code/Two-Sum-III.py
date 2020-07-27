class TwoSum(object, ):

    def __init__(self):
        self.db = {}

    def add(self, number):
        if (number not in self.db):
            self.db[number] = 0
        self.db[number] += 1

    def find(self, value):
        for (k, val) in self.db.iteritems():
            if ((value - k) == k):
                if (self.db[k] > 1):
                    return True
            elif ((value - k) in self.db):
                return True
        return False
        return (value in self.db)