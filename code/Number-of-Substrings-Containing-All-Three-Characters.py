class Solution(object):

    def numberOfSubstrings(self, s):
        self.left = 0
        self.right = 0

        def check(db):
            return ((db.get('a', 0) > 0) and (db.get('b', 0) > 0) and (db.get('c', 0) > 0))
        current = {}
        self.count = 0
        while ((self.right < len(s)) and (self.left <= self.right)):
            current[s[self.right]] = (current.get(s[self.right], 0) + 1)
            if check(current):
                self.count += (len(s) - self.right)
                current[s[self.left]] -= 1
                self.left += 1
                current[s[self.right]] -= 1
            else:
                self.right += 1
        return self.count