class Solution(object):

    def diStringMatch(self, S):
        curr_min = 0
        curr_max = len(S)
        a = []
        for letter in S:
            if (letter == 'I'):
                a.append(curr_min)
                curr_min += 1
            else:
                a.append(curr_max)
                curr_max -= 1
        a.append(curr_max)
        return a