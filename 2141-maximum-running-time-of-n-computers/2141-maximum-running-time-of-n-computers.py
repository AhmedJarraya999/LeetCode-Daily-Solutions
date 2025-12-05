class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l=1
        r=sum(batteries)//n
        while l<r:
            target = (l + r + 1) // 2
            available=0
            for b in batteries:
                available+=min(target,b)
            if available//n>=target:
                l=target
            else:
                r=target-1

        return l
        