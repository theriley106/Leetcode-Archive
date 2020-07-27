class FindElements(object, ):

    def __init__(self, root):
        self.AllVals = set()
        root.val = 0
        self.traverse(root)
        print self.AllVals

    def traverse(self, root):
        if (root == None):
            return
        if (root.right != None):
            root.right.val = ((root.val * 2) + 2)
            self.AllVals.add(root.right.val)
            self.traverse(root.right)
        if (root.left != None):
            root.left.val = ((root.val * 2) + 1)
            self.AllVals.add(root.left.val)
            self.traverse(root.left)
        self.AllVals.add(root.val)

    def find(self, target):
        return (target in self.AllVals)