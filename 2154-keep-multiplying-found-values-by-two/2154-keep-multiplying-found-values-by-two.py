class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        seen = set(nums)
        
        while original in seen:
            original *= 2
        
        return original
