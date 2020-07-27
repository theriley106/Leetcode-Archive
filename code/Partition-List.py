class Solution(object):

    def partition(self, head, check):
        a = []
        tHead = head
        while tHead:
            a.append(tHead.val)
            tHead = tHead.next
        l1 = [x for x in a if (x < check)]
        l2 = [x for x in a if (x >= check)]
        a = (l1 + l2)

        def fill():
            if (len(a) == 0):
                return None
            x = ListNode(a.pop(0))
            x.next = fill()
            return x
        return fill()