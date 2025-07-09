class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        from collections import deque
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # Step 1: Append a dummy meeting at the end to represent event end
        if eventTime > endTime[-1]:
            startTime.append(eventTime)
            endTime.append(eventTime)
        
        n = len(startTime)
        max_sum = 0
        win_sum = 0
        pos = 0
        last_end = 0
        dq = deque()

        while pos < n:
            # Calculate free time (gap between this meeting and last end)
            gap = startTime[pos] - last_end

            max_sum = max(max_sum, win_sum + gap)
            win_sum += gap
            dq.append(gap)

            # Keep window size to k
            if len(dq) > k:
                win_sum -= dq.popleft()
            
            last_end = endTime[pos]
            pos += 1

        return max_sum
