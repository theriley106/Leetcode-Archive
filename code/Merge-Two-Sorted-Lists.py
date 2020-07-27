class Solution(object):

    def mergeTwoLists(self, l1, l2):
        a = []
        while l1:
            if (l2 != None):
                if (l1.val < l2.val):
                    a.append(l1.val)
                    l1 = l1.next
                else:
                    a.append(l2.val)
                    l2 = l2.next
            else:
                a.append(l1.val)
                l1 = l1.next
        while l2:
            if (l1 != None):
                if (l1.val < l2.val):
                    a.append(l1.val)
                    l1 = l1.next
                else:
                    a.append(l2.val)
                    l2 = l2.next
            else:
                a.append(l2.val)
                l2 = l2.next

        def fill():
            if (len(a) == 0):
                return None
            else:
                h = ListNode(a.pop(0))
            h.next = fill()
            return h
        return fill()