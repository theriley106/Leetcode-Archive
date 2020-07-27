import itertools


class CombinationIterator(object, ):

    def __init__(self, characters, combinationLength):
        self.vals = list(itertools.combinations(
            list(characters), combinationLength))

    def next(self):
        return ''.join(self.vals.pop(0))

    def hasNext(self):
        return (len(self.vals) > 0)
