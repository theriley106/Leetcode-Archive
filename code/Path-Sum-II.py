class Solution(object):

    def pathSum(self, root, sumVal):
        paths = []

        def check(root, prev=[], totalSum=0):
            if (root == None):
                return
            if ((root.left == None) and (root.right == None)):
                if ((totalSum + root.val) == sumVal):
                    paths.append((prev + [root.val]))
                return
            check(root.left, (prev + [root.val]), (totalSum + root.val))
            check(root.right, (prev + [root.val]), (totalSum + root.val))
        check(root)
        return paths