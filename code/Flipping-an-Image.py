class Solution(object):

    def flipAndInvertImage(self, A):
        E = []
        for val in A:
            tmp = []
            for l in val[::(-1)]:
                if (l == 1):
                    tmp.append(0)
                else:
                    tmp.append(1)
            E.append(tmp)
        return E