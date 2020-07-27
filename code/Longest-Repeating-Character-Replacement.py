class Solution(object):

    def characterReplacement(self, s, k):
        self.left = 0
        self.right = 0
        self.max = 0
        self.db = []
        self.counts = {}
        while (self.right < len(s)):
            if (s[self.right] not in self.counts):
                self.counts[s[self.right]] = 0
            self.counts[s[self.right]] += 1
            while ((sum(self.counts.values()) - max(self.counts.values())) > k):
                self.counts[s[self.left]] -= 1
                self.left += 1
            self.max = max(self.max, sum(self.counts.values()))
            self.right += 1
        return self.max