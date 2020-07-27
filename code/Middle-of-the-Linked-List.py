class Solution(object):

    def middleNode(self, head):
        a = 0
        tempHead = head
        while tempHead:
            a += 1
            tempHead = tempHead.next
        for i in range((a / 2)):
            head = head.next
        return head