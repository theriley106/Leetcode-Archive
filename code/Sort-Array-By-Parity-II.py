class Solution(object):

    def sortArrayByParityII(self, A):
        all_evens = sorted([x for x in A if ((x % 2) == 0)])
        all_odds = sorted([x for x in A if ((x % 2) != 0)])
        all_nums = []
        for i in range((len(A) / 2)):
            all_nums.append(all_evens.pop(0))
            all_nums.append(all_odds.pop(0))
        return all_nums