class Solution(object):

    def numTeams(self, rating):
        db = {}

        def check(values, ratingsLeft, increase=False):
            if (len(ratingsLeft) == 0):
                return
            if (len(values) == 2):
                for v in ratingsLeft:
                    if increase:
                        if (v > values[(-1)]):
                            db[str((values + [v]))] = True
                    elif (v < values[(-1)]):
                        db[str((values + [v]))] = True
            else:
                for (i, v) in enumerate(ratingsLeft):
                    if (len(values) == 0):
                        check((values + [v]), ratingsLeft[(i + 1):])
                    else:
                        check(
                            (values + [v]), ratingsLeft[(i + 1):], (v > values[(-1)]))
        check([], rating)
        return len(db)
