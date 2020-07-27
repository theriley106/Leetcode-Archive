class Solution(object):

    def areSentencesSimilar(self, words1, words2, pairs):
        db = {}
        if (len(words1) != len(words2)):
            return False
        for val in pairs:
            if (val[0] not in db):
                db[val[0]] = []
            db[val[0]].append(val[1])
            if (val[1] not in db):
                db[val[1]] = []
            db[val[1]].append(val[0])
        for i in range(len(words1)):
            if (words1[i] == words2[i]):
                pass
            elif (words1[i] not in db.get(words2[i], [])):
                return False
        return True