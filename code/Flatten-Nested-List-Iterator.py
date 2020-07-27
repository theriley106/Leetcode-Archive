class NestedIterator(object, ):

    def __init__(self, nestedList):

        def getR(a):
            final = []
            if (type(a) == list):
                for val in a:
                    if (val.isInteger() == False):
                        final += getR(val)
                    else:
                        final.append(val.getInteger())
            else:
                x = a.getInteger()
                if (x == None):
                    for val in a.getList():
                        final += getR(val)
                else:
                    final.append(x)
            return final
        print nestedList
        self.listVal = getR(nestedList)
        print self.listVal

    def next(self):
        return self.listVal.pop(0)

    def hasNext(self):
        return (len(self.listVal) > 0)