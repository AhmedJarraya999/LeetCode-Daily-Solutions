class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        # Sort events by start time
        events.sort()
        # Extract the start times for binary search
        start_times = [event[0] for event in events]
        n = len(events)

        @lru_cache(None)
        def dp(index: int, remaining: int) -> int:
            if index == n or remaining == 0:
                return 0

            # Option 1: Skip the current event
            skip = dp(index + 1, remaining)

            # Option 2: Attend the current event
            _, end, value = events[index]
            # Find next event that starts after the current one ends
            next_index = bisect.bisect_right(start_times, end)
            attend = value + dp(next_index, remaining - 1)

            return max(skip, attend)

        return dp(0, k)

        