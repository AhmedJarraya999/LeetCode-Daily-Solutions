from bisect import bisect_left

class Solution:
    def maxTaskAssign(self, tasks: list[int], workers: list[int], pills: int, strength: int) -> int:
        tasks.sort()
        workrs = sorted(workers)

        def can(k):
            needed = tasks[:k]
            available = workrs[-k:]
            pool = available[:]
            p = pills

            for req in reversed(needed):
                idx = bisect_left(pool, req)
                if idx < len(pool):
                    pool.pop(idx)
                    continue

                need_with_pill = req - strength
                idx = bisect_left(pool, need_with_pill)
                if idx < len(pool) and p > 0:
                    p -= 1
                    pool.pop(idx)
                    continue

                return False

            return True

        left = 0
        right = min(len(tasks), len(workers))

        while left < right:
            mid = (left + right + 1) // 2
            if can(mid):
                left = mid
            else:
                right = mid - 1

        return left
