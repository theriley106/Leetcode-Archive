class Solution(object):

    def countCharacters(self, words, chars):
        db = {}
        for val in chars:
            if (val not in db):
                db[val] = 0
            db[val] += 1

        def comp(smallDict, largeDict=None):
            if (largeDict == None):
                largeDict = db
            for (k, v) in smallDict.iteritems():
                if ((k not in largeDict) or (v > largeDict[k])):
                    return False
            return True
        a = []
        for word in words:
            db1 = {}
            for letter in word:
                if (letter not in db1):
                    db1[letter] = 0
                db1[letter] += 1
            if (comp(db1) == True):
                a.append(word)
        print a
        return sum([len(x) for x in a])