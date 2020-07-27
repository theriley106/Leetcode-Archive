class Solution(object):

    def kthFactor(self, n, k):
        count = 0
        currentNum = (-1)
        for i in range(1, (n + 1)):
            if ((n % i) == 0):
                count += 1
                currentNum = i
            if (count == k):
                return currentNum
        return (-1)