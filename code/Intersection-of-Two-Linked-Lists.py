class Solution(object):

    def getIntersectionNode(self, headA, headB):
        info = {}
        while headA:
            info[headA] = None
            headA = headA.next
        while headB:
            if (headB in info):
                return headB
            headB = headB.next