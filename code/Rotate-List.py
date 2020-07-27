class Solution(object):

    def rotateRight(self, head, k):
        a = []
        while head:
            a.append(head.val)
            head = head.next
        if (len(a) > 0):
            for i in xrange((k % len(a))):
                a.insert(0, a.pop((-1)))
        return a