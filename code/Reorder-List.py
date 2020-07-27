class Solution(object):

    def reorderList(self, head):
        a = []
        tHead = head
        while tHead:
            a.append(tHead)
            tHead = tHead.next

        def fill(h, index=0):
            print index
            if (len(a) == 0):
                return None
            if ((index % 2) == 0):
                h = a.pop(0)
            else:
                h = a.pop((-1))
            h.next = fill(h, (index + 1))
            return h
        head = fill(head)
        return head