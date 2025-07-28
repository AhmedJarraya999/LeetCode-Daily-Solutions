class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        res=False
        for i in range(len(nums)):
            if i<=len(nums)-3:
                if nums[i]<nums[i+1] and nums[i+1]<nums[i+2]:
                    res=True
        return res










































        # first = float('inf')
        # second = float('inf')

        # for num in nums:
        #     if num <= first:
        #         first = num
        #     elif num <= second:
        #         second = num
        #     else:
        #         # Found a number greater than both first and second
        #         return True
        
        # return False
