import itertools


class Solution(object):

    def generateParenthesis(self, n):
        self.max = (n * 2)
        a = {')': '('}
        self.vals = []

        def is_valid(parenString):
            stack = []
            for letter in parenString:
                if (len(stack) == 0):
                    stack.append(letter)
                elif (stack[(-1)] == a.get(letter)):
                    stack.pop((-1))
                else:
                    stack.append(letter)
            return (len(stack) == 0)
        vals = (['(' for i in range(n)] + [')' for i in range(n)])

        def create(n, stack=['('], val='', left=None):
            if (left == None):
                left = vals
            left.remove(stack[(-1)])
            val += stack[(-1)]
            if (len(val) == self.max):
                if (is_valid(val) == True):
                    self.vals.append(val)
            if (')' in left):
                create(n, (stack + [')']), val, list(left))
            if ('(' in left):
                create(n, (stack + ['(']), val, list(left))
        create(n)
        return self.vals
