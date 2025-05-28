class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        prevEnd=0
        for start,end in meetings:
            start=max(prevEnd+1,start)
            length=end-start+1
            days-=max(length,0)
            prevEnd=max(prevEnd,end)
        return days


        # vacation_days = set()
        # for start, end in meetings:
        #     for day in range(start, end + 1):
        #         vacation_days.add(day)
        
        # return days - len(vacation_days)

        