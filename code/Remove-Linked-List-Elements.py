class Solution(object):

    def removeElements(self, head, val):
        headVals = []
        while head:
            if (head.val != val):
                headVals.append(head.val)
            head = head.next
        return headVals