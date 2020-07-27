class Solution(object):

    def reverseList(self, head):
        a = None
        while head:
            tmpHead = head
            head = head.next
            tmpHead.next = a
            a = tmpHead
        return a