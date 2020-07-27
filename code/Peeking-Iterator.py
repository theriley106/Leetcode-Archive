class PeekingIterator(object, ):

    def __init__(self, iterator):
        self.listVal = []
        while iterator.hasNext():
            self.listVal.append(iterator.next())

    def peek(self):
        return self.listVal[0]

    def next(self):
        return self.listVal.pop(0)

    def hasNext(self):
        return (len(self.listVal) != 0)