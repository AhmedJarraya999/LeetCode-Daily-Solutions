class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        odd_count=1 if nums[0]%2==1 else 0
        even_count=1 if nums[0]%2==0 else 0 
        alternating_count=1
        expect_even=True if nums[0]%2==1 else False
        for i in range(1,len(nums)):
            if (expect_even==True and nums[i]%2==0) or (expect_even==False and nums[i]%2==1):
                alternating_count+=1
                expect_even= not expect_even
            if nums[i]%2==0:
                even_count+=1
            else:
                odd_count+=1
        return max(alternating_count,odd_count,even_count)



