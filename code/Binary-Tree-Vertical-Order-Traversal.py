class Solution(object):

    def verticalOrder(self, root):
        db = {}
        self.minWidth = 0
        self.maxWidth = 0
        self.maxLength = 0
        self.count = 0

        def traverse(root, row=0, column=0):
            if (root == None):
                return
            if (row > self.maxLength):
                self.maxLength = row
            if (column > self.maxWidth):
                self.maxWidth = column
            if (column < self.minWidth):
                self.minWidth = column
            traverse(root.left, (row + 1), (column - 1))
            if ((row, column) not in db):
                db[(row, column)] = []
            db[(row, column)].append(root.val)
            self.count += 1
            traverse(root.right, (row + 1), (column + 1))
        traverse(root)
        matrix = [[[] for i in range(len(range(
            self.minWidth, (self.maxWidth + 1))))] for e in range((self.maxLength + 1))]
        for rowIndex in range(len(matrix)):
            for columnIndex in range(len(matrix[0])):
                matrix[rowIndex][columnIndex] += db.get(
                    (rowIndex, (self.minWidth + columnIndex)), [])
            print matrix[rowIndex]
        a = []
        if ((len(matrix) == 0) or (self.count == 0)):
            return []
        for columnIndex in range(len(matrix[0])):
            temp = []
            for rowIndex in range(len(matrix)):
                temp += matrix[rowIndex][columnIndex]
            a.append(temp)
        return a
        print self.maxWidth
        print self.minWidth
        print self.maxLength
        print db
