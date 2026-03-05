class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        lowest=nums[1]
        secondlowest=float('inf')
        for i in range(2,len(nums)):
            if nums[i]<lowest:
                secondlowest=lowest
                lowest=nums[i]
            elif nums[i]<secondlowest:
                secondlowest=nums[i]
        return nums[0]+lowest+secondlowest

        

        

        
                
            

        