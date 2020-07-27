class Solution(object):

    def maxNumberOfBalloons(self, text):

        def is_balloon(db):
            x = True
            x = (x and (db.get('b', 0) >= 1))
            x = (x and (db.get('a', 0) >= 1))
            x = (x and (db.get('l', 0) >= 2))
            x = (x and (db.get('o', 0) >= 2))
            x = (x and (db.get('n', 0) >= 1))
            return x
        count = 0
        text = list(text)
        db = {}
        for val in text:
            if (val not in db):
                db[val] = 0
            db[val] += 1
        while (is_balloon(db) == True):
            db['b'] = (db['b'] - 1)
            db['l'] = (db['l'] - 2)
            db['a'] = (db['a'] - 1)
            db['o'] = (db['o'] - 2)
            db['n'] = (db['n'] - 1)
            count += 1
        return count