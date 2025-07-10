from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        available_space = [False] * n

        s1 = 0
        # Forward pass: check if a meeting can be shifted forward
        for i in range(n):
            if endTime[i] <= startTime[i] and endTime[i] <= s1:
                available_space[i] = True
            s1 = max(s1, 0 if i == 0 else endTime[i - 1])

        s2 = 0
        # Backward pass: check if a meeting can be shifted backward
        for i in range(n - 1, -1, -1):
            if endTime[i] <= startTime[i] and startTime[i] >= s2:
                available_space[i] = True
            s2 = max(s2, eventTime if i == n - 1 else startTime[i + 1])

        res = 0
        for i in range(n):
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]

            if available_space[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))

        return res
