class Solution(object):

    def numSub(self, s):
        return (sum([((len(x) * (len(x) + 1)) / 2) for x in str(s).split('0')]) % ((10 ** 9) + 7))