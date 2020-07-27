class Solution(object):

    def numKLenSubstrNoRepeats(self, S, K):
        count = 0
        db = {}
        if (len(S) < K):
            return 0
        for val in S:
            db[val] = 0
        for i in range(K):
            if (S[i] not in db):
                db[S[i]] = 0
            db[S[i]] += 1
        if (max(db.values()) == 1):
            count += 1
        for i in range(1, ((len(S) - K) + 1)):
            if (len(S[i:(i + K)]) != K):
                break
            db[S[((i + K) - 1)]] += 1
            db[S[(i - 1)]] = (db[S[(i - 1)]] - 1)
            if ((max(db.values()) == 1) and (len(S[i:(i + K)]) == K)):
                print db
                print S[i:(i + K)]
                count += 1
        return count