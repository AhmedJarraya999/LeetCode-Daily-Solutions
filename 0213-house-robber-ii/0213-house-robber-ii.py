class Solution(object):
    @staticmethod
    #no need to pass self as argument
    def helper(nums):
            rob1,rob2=0,0
            for num in nums:
                temp=max(rob1+num,rob2)
                rob1=rob2
                rob2=temp
            return rob2
    def rob(self, nums):
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
        