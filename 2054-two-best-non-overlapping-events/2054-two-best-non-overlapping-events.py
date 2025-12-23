class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n=len(events)
        starts = [e[0] for e in events]  
        @lru_cache(None)
        def dp(i,k):
            if i==n or k==0:
                return 0
            #skip curr event
            ans=dp(i+1,k)
            #attend next_event
            next_index=bisect_right(starts,events[i][1])
            ans=max(ans,events[i][2]+dp(next_index,k-1))
            return ans
        return dp(0,2)