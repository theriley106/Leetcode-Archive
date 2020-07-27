class Solution(object):

    def confusingNumber(self, N):
        a = ['0', '1', '6', '8', '9']
        for val in str(N):
            if (val not in a):
                return False
        g = str(N)
        g = g.replace('6', 'R')
        g = g.replace('9', '6')
        g = g.replace('R', '9')
        print g
        print str(N)
        if (g[::(-1)] == str(N)):
            return False
        return True
        return (('6' in str(N)) or ('9' in str(N)))