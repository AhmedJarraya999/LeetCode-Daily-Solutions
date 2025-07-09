class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        durations = [end - start for start, end in zip(startTime, endTime)]

        @lru_cache(None)
        def dfs(i: int, k_left: int, curr_time: int) -> int:
            if i == n:
                return eventTime - curr_time  # remaining free time at the end

            max_gap = 0

            # Option 1: Do not reschedule meeting i
            normal_start = max(curr_time, startTime[i])
            normal_end = normal_start + durations[i]
            gap = normal_start - curr_time  # free time before this meeting
            max_gap = max(max_gap, gap)
            max_gap = max(max_gap, dfs(i + 1, k_left, normal_end))

            # Option 2: Reschedule meeting i (if possible)
            if k_left > 0:
                resched_start = curr_time
                resched_end = resched_start + durations[i]
                max_gap = max(max_gap, dfs(i + 1, k_left - 1, resched_end))

            return max_gap

        return dfs(0, k, 0)
        