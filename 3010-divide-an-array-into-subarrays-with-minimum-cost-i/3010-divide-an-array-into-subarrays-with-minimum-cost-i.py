class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # nums.sort()
        # cnt=0
        # tot=0
        # i=0
        # while cnt<3:
        #     tot+=nums[i]
        #     i+=1
        #     cnt+=1
        # return tot
        lowest=nums[1]
        secondlowest=float('inf')
        for i in range(2,len(nums)):
            if nums[i]<lowest:
                secondlowest=lowest
                lowest=nums[i]
            elif nums[i]<secondlowest:
                secondlowest=nums[i]
        return nums[0]+lowest+secondlowest
                
            

        