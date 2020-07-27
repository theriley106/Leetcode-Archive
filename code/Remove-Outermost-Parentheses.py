class Solution(object):

    def removeOuterParentheses(self, S):
        a = []
        b = []
        temp = []
        v = {'(': ')', ')': '('}
        for (i, val) in enumerate(S):
            if (len(a) == 0):
                temp.append([])
            temp[(-1)].append(val)
            if (len(a) > 0):
                if (a[(-1)] == v[val]):
                    a.pop((-1))
                else:
                    a.append(val)
            else:
                a.append(val)
        x = ''
        for val in temp:
            x += ''.join(val[1:(-1)])
        return x