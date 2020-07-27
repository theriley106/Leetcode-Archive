class Solution(object):

    def sortedListToBST(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next

        def insert(nums):
            if (len(nums) == 0):
                return
            centerPoint = (len(nums) / 2)
            root = TreeNode(nums[centerPoint])
            root.right = insert(nums[(centerPoint + 1):])
            root.left = insert(nums[:centerPoint])
            return root
        root = insert(a)
        return root