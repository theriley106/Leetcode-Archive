class Solution(object):

    def reverseKGroup(self, head, k):
        a = []
        tHead = head
        while tHead:
            a.append(tHead.val)
            tHead = tHead.next
        for i in range(0, len(a), k):
            if ((i + k) <= len(a)):
                a[i:(i + k)] = a[i:(i + k)][::(-1)]

        def fill():
            if (len(a) == 0):
                return None
            x = ListNode(a.pop(0))
            x.next = fill()
            return x
        head = fill()
        return head