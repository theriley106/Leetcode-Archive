class Solution(object):

    def minAddToMakeValid(self, S):
        stack = []
        for val in S:
            if ((len(stack) > 0) and (stack[(-1)] == '(') and (val == ')')):
                stack.pop()
            else:
                stack.append(val)
        return len(stack)