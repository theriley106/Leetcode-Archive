class Solution(object):

    def lengthOfLongestSubstringKDistinct(self, s, k):
        db = {}
        self.left = 0
        self.right = 0

        def is_valid():
            return len([x for (x, i) in db.iteritems() if (i != 0)])
        maxSize = 0
        while ((self.left <= self.right) and (self.right < len(s))):
            db[s[self.right]] = (db.get(s[self.right], 0) + 1)
            self.right += 1
            size = is_valid()
            if (is_valid() <= k):
                if ((self.right - self.left) > maxSize):
                    maxSize = (self.right - self.left)
            while (size > k):
                db[s[self.left]] -= 1
                self.left += 1
                size = is_valid()
        return maxSize