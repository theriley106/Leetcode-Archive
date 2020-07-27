class Solution(object):

    def getTargetCopy(self, original, cloned, target):
        self.solved = None

        def t(root):
            if (root == None):
                return []
            return ((t(root.left) + [root.val]) + t(root.right))
        self.root_target = t(target)

        def traverse(root):
            if (root == None):
                return []
            if (root == target):
                self.solved = root
            a = ((traverse(root.left) + [root.val]) + traverse(root.right))
            if (a == self.root_target):
                self.solved = root
            return a
        traverse(cloned)
        return self.solved