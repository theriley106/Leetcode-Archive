class Solution(object):

    def getDecimalValue(self, head):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return int(''.join([str(x) for x in a]), 2)
        print a