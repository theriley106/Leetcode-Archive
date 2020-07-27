class Solution(object):

    def cloneTree(self, root):

        def clone(root):
            if (root == None):
                return
            newRoot = Node(root.val)
            for v in root.children:
                newRoot.children.append(clone(v))
            return newRoot
        return clone(root)