class Solution(object):

    def deleteNodes(self, head, m, n):
        e = []
        currentM = m
        currentN = n
        while head:
            r = head.val
            if ((currentN == 0) and (currentM == 0)):
                currentM = m
                currentN = n
            if (currentM == 0):
                currentN = (currentN - 1)
            else:
                e.append(r)
                currentM = (currentM - 1)
            head = head.next

        def fill():
            if (len(e) == 0):
                return None
            listVal = ListNode(e.pop(0))
            listVal.next = fill()
            return listVal
        return fill()