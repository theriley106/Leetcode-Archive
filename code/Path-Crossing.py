class Solution(object):

    def isPathCrossing(self, path):
        startPoint = [0, 0]
        db = {str([0, 0]): 1}
        for v in path:
            if (v == 'N'):
                startPoint[0] += 1
            elif (v == 'E'):
                startPoint[1] += 1
            elif (v == 'S'):
                startPoint[0] -= 1
            else:
                startPoint[1] -= 1
            if (str(startPoint) not in db):
                db[str(startPoint)] = 0
            db[str(startPoint)] += 1
            print str(startPoint)
        print db
        return (max(db.values()) > 1)