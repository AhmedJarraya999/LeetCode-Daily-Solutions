class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def digit_sum(n):
            return sum(int(d) for d in str(abs(n))) 
        for i,num in enumerate(nums):
            if digit_sum(num)==i:
                return i
        return -1
              
        
        