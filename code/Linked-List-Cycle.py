class Solution(object):

    def hasCycle(self, head):
        while head:
            a = None
            try:
                a = head.visited
            except:
                head.visited = True
            print head.val
            head = head.next
            if (a != None):
                return True
        return False