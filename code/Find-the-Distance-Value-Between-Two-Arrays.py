class Solution(object):

    def findTheDistanceValue(self, arr1, arr2, d):

        def is_true(num1, num2):
            return (abs((num1 - num2)) > d)
        count = 0
        for v in arr1:
            a = True
            for g in arr2:
                a = (a and is_true(v, g))
            if (a == True):
                count += 1
        return count