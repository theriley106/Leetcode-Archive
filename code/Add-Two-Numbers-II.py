class Solution(object):

    def addTwoNumbers(self, l1, l2):
        a = []
        b = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        while l2:
            b.append(l2.val)
            l2 = l2.next
        a = int(''.join([str(x) for x in a]))
        b = int(''.join([str(x) for x in b]))
        c = (a + b)
        g = list([int(x) for x in str(c)])
        return g