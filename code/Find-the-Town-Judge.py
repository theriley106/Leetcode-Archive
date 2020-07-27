class Solution(object):

    def findJudge(self, N, trust):
        self.people = {}
        for i in range(1, (N + 1)):
            self.people[str(i)] = []
        for val in trust:
            self.people[str(val[0])].append(val[1])
        for (key, val) in self.people.iteritems():
            if (len(val) == 0):
                totalCount = 0
                for val in [i for i in range(1, (N + 1)) if (i != int(key))]:
                    if (int(key) in self.people[str(val)]):
                        totalCount += 1
                if (totalCount == (len(self.people) - 1)):
                    return int(key)
        return (-1)