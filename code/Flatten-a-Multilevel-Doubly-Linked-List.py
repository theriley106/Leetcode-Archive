class Solution(object):

    def flatten(self, head):

        def f(h):
            a = []
            while (h != None):
                if (h.child == None):
                    a += [h.val]
                else:
                    a += ([h.val] + f(h.child))
                h = h.next
            return a
        a = []
        a += f(head)

        def fill(prev=None):
            if (len(a) == 0):
                return None
            g = a.pop(0)
            x = Node(g, prev, None, None)
            x.next = fill(x)
            return x
        e = fill()
        return e