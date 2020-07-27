class Solution(object):

    def __init__(self):
        self.isTrue = False

    def twoSumBSTs(self, root1, root2, target):
        db = {}

        def traverse(root):
            if (root == None):
                return
            db[root.val] = True
            traverse(root.left)
            traverse(root.right)

        def traverse2(root, target):
            if (root == None):
                return
            if ((target - root.val) in db):
                self.isTrue = True
            traverse2(root.left, target)
            traverse2(root.right, target)
        traverse(root1)
        traverse2(root2, target)
        return self.isTrue