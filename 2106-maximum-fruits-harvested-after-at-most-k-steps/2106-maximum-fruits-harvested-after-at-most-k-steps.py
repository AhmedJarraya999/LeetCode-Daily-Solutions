from bisect import bisect_right
from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        
        # Step 1: Split into left and right relative to startPos
        left, right = [], []
        i = 0
        while i < n and fruits[i][0] <= startPos:
            dist = startPos - fruits[i][0]
            cnt  = fruits[i][1]
            left.append([dist, cnt])
            i += 1
        left.reverse()
        
        while i < n:
            dist = fruits[i][0] - startPos
            cnt  = fruits[i][1]
            right.append([dist, cnt])
            i += 1
        
        # Step 2: Build prefix sums
        psumL = [0] * (len(left) + 1)
        psumR = [0] * (len(right) + 1)
        for idx, (_, cnt) in enumerate(left):
            psumL[idx+1] = psumL[idx] + cnt
        for idx, (_, cnt) in enumerate(right):
            psumR[idx+1] = psumR[idx] + cnt
        
        # Helper: count how many entries have distance ≤ steps
        def count_le(arr: List[List[int]], steps: int) -> int:
            # arr is sorted by arr[*][0]
            dists = [d for d, _ in arr]
            return bisect_right(dists, steps)
        
        # Step 3: Try all splits of steps between left/right trips
        max_collected = 0
        for go in range(k + 1):
            # go left first
            left_count  = count_le(left, go)
            right_count = count_le(right, k - 2*go)
            max_collected = max(max_collected,
                                psumL[left_count] + psumR[right_count])
            
            # go right first
            right_count = count_le(right, go)
            left_count  = count_le(left, k - 2*go)
            max_collected = max(max_collected,
                                psumL[left_count] + psumR[right_count])
        
        return max_collected

