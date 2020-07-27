class Solution(object):

    def canFinish(self, numCourses, prerequisites):
        db = {}
        for course in range(numCourses):
            db[course] = set()
        coursesToTake = db.keys()
        for val in prerequisites:
            db[val[0]].add(val[1])
        courses_taken = set()
        prevlen = None
        while (len(courses_taken) != prevlen):
            prevlen = len(courses_taken)
            for (k, v) in db.iteritems():
                r = (db[k] - courses_taken)
                if (len(r) == 0):
                    courses_taken.add(k)
        return (len(courses_taken) == len(coursesToTake))
        print db