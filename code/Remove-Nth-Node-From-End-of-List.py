class Solution(object):

    def removeNthFromEnd(self, head, n):
        list_vals = []
        while head:
            list_vals.append(head.val)
            head = head.next
        list_vals.pop((- n))
        return list_vals