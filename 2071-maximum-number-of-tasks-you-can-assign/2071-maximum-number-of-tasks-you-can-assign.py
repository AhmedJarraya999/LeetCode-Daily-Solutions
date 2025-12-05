class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        tasks=sorted(tasks)
        workrs=sorted(workers)
        def can(k):
            needed=tasks[:k]
            available=workers[-k:]
            pool = available[:] 
            p = pills
            for req in reversed(needed):
                idx=bisect_left(pool,req)
                if idx<len(pool):
                    pool.pop(idx)
                    continue
                needed_with_pill=req-strength
                idx=bisect_left(pool,needed_with_pill)
                if idx<len(pool) and p>0:
                    p-=1
                    pool.pop(idx)
                    continue
                return False
            return True
        left=0
        right=min(len(tasks),len(workers))
        while left<right:
            mid=(left+right+1)//2
            if can(mid):
                left=mid
            else:
                right=mid-1
        return left








        