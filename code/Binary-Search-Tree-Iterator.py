class BSTIterator(object, ):

    def __init__(self, root):
        self.a = []

        def f(root):
            if (root == None):
                return
            self.a.append(root.val)
            f(root.left)
            f(root.right)
        f(root)
        self.a.sort()

    def next(self):
        return self.a.pop(0)

    def hasNext(self):
        return (len(self.a) > 0)