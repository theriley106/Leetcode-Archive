class Solution(object):

    def isSubPath(self, head, root):

        def traverse(root, currentPath=[]):
            if (currentPath[(- self.length):] == self.vals):
                return True
            if (root == None):
                return False
                x = False
            return (traverse(root.left, (currentPath + [root.val])) or traverse(root.right, (currentPath + [root.val])))
        self.vals = []
        while head:
            self.vals.append(head.val)
            head = head.next
        self.length = len(self.vals)
        return traverse(root)