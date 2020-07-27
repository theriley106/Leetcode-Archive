class Solution(object):

    def sortTransformedArray(self, nums, a, b, c):

        def quadratic_equation(val):
            return (((a * (val ** 2)) + (b * val)) + c)
        return sorted(map(quadratic_equation, nums))