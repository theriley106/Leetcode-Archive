class Solution(object):

    def findOcurrences(self, text, first, second):
        x = text.split(' ')
        return [x[(i + 2)] for i in range((len(x) - 2)) if ((x[i] == first) and (x[(i + 1)] == second))]