class Solution(object):

    def customSortString(self, S, T):
        S = (list(S) + [val for val in (set(T) - set(S))])
        return ''.join(sorted(T, key=(lambda k: list(S).index(k))))