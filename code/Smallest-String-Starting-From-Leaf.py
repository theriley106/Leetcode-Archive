class Solution(object):

    def smallestFromLeaf(self, root):
        string.ascii_lowercase
        self.vals = []

        def traverse(root, prev=''):
            if (root == None):
                return
            isLeaf = ((root.left == None) and (root.right == None))
            if isLeaf:
                x = (prev + string.ascii_lowercase[root.val])
                print x
                self.vals.append(x[::(-1)])
                return
            traverse(root.left, (prev + string.ascii_lowercase[root.val]))
            traverse(root.right, (prev + string.ascii_lowercase[root.val]))
        traverse(root)
        return sorted(self.vals)[0]
        print self.vals