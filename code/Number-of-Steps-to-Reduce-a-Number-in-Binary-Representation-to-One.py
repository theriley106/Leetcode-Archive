class Solution(object):

    def numSteps(self, s):
        num = int(s, 2)

        def step(number):
            if (number == 1):
                return 0
            if ((number % 2) == 0):
                return (1 + step((number / 2)))
            return (1 + step((number + 1)))
        return step(num)