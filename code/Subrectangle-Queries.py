class SubrectangleQueries(object, ):

    def __init__(self, rectangle):
        self.rectangle = rectangle
        for v in self.rectangle:
            print v

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row1, (row2 + 1)):
            for e in range(col1, (col2 + 1)):
                self.rectangle[i][e] = newValue

    def getValue(self, row, col):
        return self.rectangle[row][col]