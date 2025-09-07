class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        tot=0
        for i in range(len(timeSeries) - 1):
            gap=timeSeries[i+1]-timeSeries[i]
            tot+=min(duration,gap)
        #ekher attack ya3ti dima duration kemla
        tot+=duration
        return tot

        