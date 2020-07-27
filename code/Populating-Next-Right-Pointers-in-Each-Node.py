class Solution(object):

    def connect(self, rootz):
        self.dbRows = {}

        def create_inorder(root, row=0, column=0):
            if (root == None):
                return
            if (row not in self.dbRows):
                self.dbRows[row] = []
            create_inorder(root.left, (row + 1), (column - 1))
            self.dbRows[row].append(root)
            create_inorder(root.right, (row + 1), (column + 1))
        create_inorder(rootz)
        self.root = rootz
        for (k, v) in self.dbRows.iteritems():
            self.dbRows[k].pop(0)
            self.dbRows[k].append(None)

        def create_inorder2(root, row=0, column=0):
            if (root == None):
                return
            create_inorder2(root.left, (row + 1), (column - 1))
            root.next = self.dbRows[row].pop(0)
            create_inorder2(root.right, (row + 1), (column + 1))
        create_inorder2(self.root)
        return self.root