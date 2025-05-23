class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        bad_numbers=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                bad_numbers.add(fronts[i])
        res=float('inf')
        for num in fronts+backs:
            if num not in bad_numbers:
                res=min(res,num)
        return res if res!=float('inf') else 0
        