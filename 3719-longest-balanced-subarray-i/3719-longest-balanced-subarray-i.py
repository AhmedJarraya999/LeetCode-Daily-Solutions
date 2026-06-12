class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            evenset=set()
            oddset=set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    evenset.add(nums[j])
                if nums[j]%2==1:
                    oddset.add(nums[j])
                if len(oddset)==len(evenset):
                    ans=max(ans,j-i+1)
        return ans
                