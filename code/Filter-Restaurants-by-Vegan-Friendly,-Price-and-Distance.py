class Solution(object):

    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        newArray = []
        for val in restaurants:
            (idVal, rating, isVeganFriendly, price, distance) = val
            if (veganFriendly == 1):
                if isVeganFriendly:
                    if ((price <= maxPrice) and (distance <= maxDistance)):
                        newArray.append(val)
                else:
                    pass
            elif ((price <= maxPrice) and (distance <= maxDistance)):
                newArray.append(val)
        db = {}
        for val in newArray:
            if (val[1] not in db):
                db[val[1]] = []
            db[val[1]].append(val[0])
        ratings = sorted(db.keys(), reverse=True)
        a = []
        for k in ratings:
            print k
            for val in sorted(db[k], reverse=True):
                a.append(val)
        return a
        return [x[0] for x in sorted(newArray, key=(lambda k: k[1]), reverse=True)]