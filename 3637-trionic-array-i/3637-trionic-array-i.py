class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        state=0
        if nums[0]>=nums[1]:
            return False
        for i in range(2,len(nums)):
            if state==0:
                if nums[i]>nums[i-1]:
                    continue
                elif nums[i]<nums[i-1]:
                    state=1
                else:
                    return False
            if state==1:
                if nums[i]<nums[i-1]:
                    continue
                elif nums[i]>nums[i-1]:
                    state=2
                else:
                    return False
            else:
                if nums[i]<=nums[i-1]:
                    return False
        return state==2
            
        