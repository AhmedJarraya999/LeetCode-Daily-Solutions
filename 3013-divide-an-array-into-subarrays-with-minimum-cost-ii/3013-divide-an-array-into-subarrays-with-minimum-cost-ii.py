from sortedcontainers import SortedList
from typing import List

class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        n = len(nums)

        small = SortedList()
        large = SortedList()

        # initial window
        for i in range(1, dist + 2):
            small.add((nums[i], i))

        while len(small) >= k:
            large.add(small.pop(-1))

        curr = sum(v for v, _ in small)
        res = curr

        for i in range(dist + 2, n):
            pkey = (nums[i - dist - 1], i - dist - 1)
            nkey = (nums[i], i)

            if pkey in small:
                small.discard(pkey)
                curr -= pkey[0]

                if large:
                    l = large.pop(0)
                    small.add(l)
                    curr += l[0]

            elif pkey in large:
                large.discard(pkey)

            small.add(nkey)
            curr += nkey[0]

            if len(small) >= k:
                s = small.pop(-1)
                large.add(s)
                curr -= s[0]

            res = min(res, curr)

        return res + nums[0]