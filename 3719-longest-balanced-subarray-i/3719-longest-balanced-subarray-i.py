class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans=0
        for i in range(len(nums)):
            even_set=set()
            odd_set=set()
            for j in range(i,len(nums)):
                if nums[j]%2==0:
                    even_set.add(nums[j])
                if nums[j]%2==1:
                    odd_set.add(nums[j])
                if len(even_set)==len(odd_set):
                    ans=max(ans,j-i+1)
        return ans
                

        

        
                    




        
