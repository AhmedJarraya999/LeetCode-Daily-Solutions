class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        lastday={} #last day we executed that task
        day=1
        for t in tasks:
            if t in lastday:
                earliest=lastday[t]+space+1 
                if day<earliest:
                    day=earliest
            lastday[t]=day
            day+=1  
        return day-1
            



        