class Solution(object):
    def minDifference(self, nums):
        if len(nums) < 4:
            return 0
        # nums = [1,5,0,10,14]
        #print 
        nums = nums[-4:] + nums[4:]
        self.min = float("inf")
        
        for val in itertools.combinations(list(range(len(nums))), 3):
            x = list(nums)
            for t in val:
                x[t] = None
            x = [d for d in x if d != None]
            self.min = min(self.min, max(x) - min(x))
            
        
        return self.min
        """
        :type nums: List[int]
        :rtype: int
        """
        