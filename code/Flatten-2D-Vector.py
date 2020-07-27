import re


class Vector2D(object, ):

    def __init__(self, v):
        self.vals = re.findall('-?d+', str(v))

    def next(self):
        return self.vals.pop(0)

    def hasNext(self):
        return (len(self.vals) > 0)
