class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res=[]
        hours=[1,2,4,8]
        minutes=[1,2,4,8,16,32]
        #num_leds: how many keds chosen so far
        def backtrack(num_leds,start,h,m):
            if num_leds==0:
                if h<12 and m<60:
                    res.append(f"{h}:{m:02d}")
                return
            #itertate all leds:
            for i in range(start,len(hours)+len(minutes)):
                if i<len(hours):
                    backtrack(num_leds - 1, i + 1, h + hours[i], m)
                else:
                    backtrack(num_leds - 1, i + 1, h, m + minutes[i - len(hours)])
        backtrack(turnedOn,0,0,0)
        return res
