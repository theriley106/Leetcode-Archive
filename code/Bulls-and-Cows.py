class Solution(object):

    def getHint(self, secret, guess):
        a = 0
        b = 0
        db = {}
        for val in secret:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        values = []
        for i in range(len(secret)):
            if (secret[i] == guess[i]):
                db[guess[i]] -= 1
                a += 1
            else:
                values.append(guess[i])
        print values
        for val in values:
            if (db.get(val, 0) >= 1):
                db[val] -= 1
                b += 1
        return '{}A{}B'.format(a, b)