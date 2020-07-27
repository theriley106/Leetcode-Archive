class Solution(object):

    def circularArrayLoop(self, nums):
        startPoint = 0
        endPoint = (len(nums) - 1)
        self.found = False

        def get_element(index):
            return nums[((index - 1) % len(nums))]
        if (len(nums) < 2):
            return False

        def check(index=0, prev={}, allPositive=True, start=False, count=0):
            if (start == True):
                if (nums[index] < 0):
                    allPositive = False
            if (abs(index) >= len(nums)):
                trueIndex = (index % len(nums))
            elif (index < 0):
                trueIndex = (index % len(nums))
            else:
                trueIndex = index
            if ((nums[trueIndex] < 0) and (allPositive == True)):
                return
            if ((nums[trueIndex] > (-1)) and (allPositive == False)):
                return
            if (trueIndex in prev):
                if ((count - prev[trueIndex]) > 1):
                    self.found = True
                return
            prev[trueIndex] = count
            check((index + nums[trueIndex]), prev,
                  allPositive, count=(count + 1))
        for i in range(len(nums)):
            check(prev=dict(), index=i, start=True)
            if (self.found == True):
                return True
        return self.found
