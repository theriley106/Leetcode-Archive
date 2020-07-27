class Solution(object):

    def reverseBetween(self, head, m, n):
        listVals = []
        tHead = head
        while tHead:
            listVals.append(tHead.val)
            tHead = tHead.next
        listVals[(m - 1):n] = listVals[(m - 1):n][::(-1)]

        def fill():
            if (len(listVals) == 0):
                return None
            x = ListNode(listVals.pop(0))
            x.next = fill()
            return x
        return fill()