class Solution(object):

    def copyRandomBinaryTree(self, root):
        self.db = {}

        def traverse(root):
            if (root == None):
                return
            self.db[root] = NodeCopy(root.val, root.left, root.right)
            traverse(root.left)
            traverse(root.right)
        traverse(root)

        def copy(root):
            if (root == None):
                return
            newRoot = self.db[root]
            newRoot.random = self.db.get(root.random)
            newRoot.left = copy(root.left)
            newRoot.right = copy(root.right)
            return newRoot
        return copy(root)