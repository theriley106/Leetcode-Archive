class Solution(object):

    def mergeKLists(self, lists):
        self.lists = lists

        def reset_lists():
            self.lists = [x for x in self.lists if (x != None)]

        def get_next():
            index = 0
            lowest = float('inf')
            reset_lists()
            if (len(self.lists) == 0):
                return None
            for (i, v) in enumerate(self.lists):
                if (v.val < lowest):
                    lowest = v.val
                    index = i
            final = self.lists[index].val
            self.lists[index] = self.lists[index].next
            return final

        def fill():
            x = get_next()
            rootVal = ListNode(x)
            if (x != None):
                rootVal.val = x
                rootVal.next = fill()
            else:
                return None
            return rootVal
        return fill()