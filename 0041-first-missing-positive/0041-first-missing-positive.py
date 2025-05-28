class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        counter=Counter(nums)
        i=0
        breaker=False
        while (breaker==False):
            i+=1
            if i not in counter:
                breaker=True
                return i
            
               

        