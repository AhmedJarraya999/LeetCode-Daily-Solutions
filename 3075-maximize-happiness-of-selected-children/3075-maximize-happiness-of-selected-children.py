class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        total = 0
        
        for i in range(k):   # i starts from 0
            total += max(happiness[i] - i, 0)
        
        return total
