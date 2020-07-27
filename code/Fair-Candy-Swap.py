class Solution(object):

    def fairCandySwap(self, A, B):
        alice = sum(A)
        bob = sum(B)
        print alice
        print bob
        targetSum = ((bob + alice) / 2)
        alice_db = {}
        bob_db = {}
        for val in A:
            if (val not in alice_db):
                alice_db[val] = 0
            alice_db[val] += 1
        for val in B:
            if ((targetSum - (bob - val)) in alice_db):
                return [(targetSum - (bob - val)), val]