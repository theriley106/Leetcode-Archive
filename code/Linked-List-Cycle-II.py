class Solution(object):

    def detectCycle(self, head):
        a = {}
        while head:
            if (head in a):
                return head
            a[head] = ''
            head = head.next
        return None