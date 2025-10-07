import bisect

class Solution:
    def avoidFlood(self, rains):
        full = {}           # lake -> last rain day
        dry_days = []       # sorted list of indices where it’s dry
        ans = [-1] * len(rains)
        
        for i, lake in enumerate(rains):
            if lake == 0:
                # Mark as available dry day
                bisect.insort(dry_days, i)
                ans[i] = 1  # placeholder, will update later if needed
            else:
                if lake in full:
                    # Need to find a dry day after full[lake]
                    idx = bisect.bisect_right(dry_days, full[lake])
                    if idx == len(dry_days):
                        # No dry day available after the last rain of this lake
                        return []
                    dry_day = dry_days.pop(idx)
                    ans[dry_day] = lake  # dry this lake on that day
                # Update the last rain day
                full[lake] = i
                ans[i] = -1
        
        return ans
