class Solution(object):

    def oddEvenList(self, head):
        my_list = []
        e = 0
        info = {'odd': [], 'even': []}
        while head:
            if ((e % 2) != 0):
                info['even'].append(head.val)
            else:
                info['odd'].append(head.val)
            e += 1
            head = head.next
        my_list += info['odd']
        my_list += info['even']
        return my_list