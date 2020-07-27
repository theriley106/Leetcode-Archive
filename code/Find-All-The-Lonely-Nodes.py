class Solution(object):

    def getLonelyNodes(self, root):
        self.vals = []

        def check(root, opposite=None):
            if (root == None):
                return
            if (opposite == None):
                self.vals.append(root.val)
            check(root.left, root.right)
            check(root.right, root.left)
        check(root, 'start')
        return self.vals