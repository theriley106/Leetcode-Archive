class Solution(object):

    def lengthOfLongestSubstringTwoDistinct(self, s):
        db = {}
        self.left = 0
        self.right = 0

        def is_distinct():
            return len([x for (x, i) in db.iteritems() if (i != 0)])
        maxSize = 0
        while ((self.left <= self.right) and (self.right < len(s))):
            db[s[self.right]] = (db.get(s[self.right], 0) + 1)
            self.right += 1
            size = is_distinct()
            if (size <= 2):
                if ((self.right - self.left) > maxSize):
                    maxSize = (self.right - self.left)
            while (size > 2):
                db[s[self.left]] -= 1
                self.left += 1
                size = is_distinct()
        return maxSize