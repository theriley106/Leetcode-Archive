class Solution(object):

    def isValidSequence(self, root, arr):
        self.finished = ''.join([str(x) for x in arr])
        self.found = False

        def traverse(root, prev=''):
            if (root == None):
                return
            if (((prev + str(root.val)) == self.finished) and (root.left == None) and (root.right == None)):
                self.found = True
                return
            if (prev == self.finished[:len(prev)]):
                traverse(root.left, (prev + str(root.val)))
                traverse(root.right, (prev + str(root.val)))
        traverse(root)
        return self.found