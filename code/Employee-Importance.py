class Solution:

    def getVal(self, id, visited=[]):
        if (id in self.visited):
            return 0
        self.visited.append(id)
        value = self.dictObj[str(id)]['val']
        for val in self.dictObj[str(id)]['sub']:
            print val
            value += self.getVal(val)
        return value

    def getImportance(self, employees, id):
        self.visited = []
        self.dictObj = {}
        for val in employees:
            self.dictObj[str(val.id)] = {
                'sub': val.subordinates, 'val': val.importance}
        print self.dictObj
        return self.getVal(id)
