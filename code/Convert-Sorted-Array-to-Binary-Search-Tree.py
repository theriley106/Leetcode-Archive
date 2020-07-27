class Solution(object):

    def sortedArrayToBST(self, nums):

        def insert(numVals):
            if (len(numVals) == 0):
                return
            centerPoint = (len(numVals) / 2)
            root = ListNode(numVals[centerPoint])
            root.right = insert(numVals[(centerPoint + 1):])
            root.left = insert(numVals[:centerPoint])
            return root

        def traverse(root):
            if (root == None):
                return []
            return ((traverse(root.left) + [root.val]) + traverse(root.right))
        root = insert(nums)
        return root