class Traverse(object, ):

    def __init__(self, db):
        self.db = db
        self.visited = set()
        self.preReq = []
        self.noPrereq = set()

    def traverse(self, key):
        if (key in self.db):
            if (key not in self.visited):
                for val in self.db[key]:
                    if (val not in self.visited):
                        self.visited.add(val)
                        self.traverse(val)
        else:
            self.noPrereq.add(key)

    def reset(self):
        self.visited = set()
        self.preReq = []
        self.noPrereq = set()


class Solution(object):

    def __init__(self):
        self.courseDB = {}

    def get_nested_prereq(self, key, prev=set()):
        return

    def findOrder(self, numCourses, prerequisites):
        for courses in prerequisites:
            (course, prereq) = courses
            if (course not in self.courseDB):
                self.courseDB[course] = set()
            self.courseDB[course].add(prereq)
        keys = self.courseDB.keys()
        for i in xrange(numCourses):
            if (i not in keys):
                self.courseDB[i] = set()
        t = Traverse(self.courseDB)
        for key in keys:
            t.reset()
            t.traverse(key)
            if (len(t.noPrereq) != 0):
                for val in t.noPrereq:
                    self.courseDB[val] = set()
            for val in t.visited:
                self.courseDB[key].add(val)
        order = []
        while (len(self.courseDB) > 0):
            for (key, val) in self.courseDB.iteritems():
                if (len(val) == 0):
                    order.append(key)
                    break
            del self.courseDB[key]
            for (k, v) in self.courseDB.iteritems():
                if (key in v):
                    v.remove(key)
        if (len(order) < numCourses):
            return []
        print order
        return order
