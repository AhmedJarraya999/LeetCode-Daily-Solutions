class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD=10**9+7
        for i in range(1,len(complexity)):
            if complexity[i]<=complexity[0]:
                return 0
        return factorial(len(complexity)-1)%MOD
        

        