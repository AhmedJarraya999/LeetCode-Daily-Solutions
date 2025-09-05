class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        #straight forward did not work 
        # cnt=0
        # while startValue!=target:
        #     doubled=startValue*2
        #     substracted=startValue-1
        #     if abs(target-doubled)<abs(target-substracted):
        #         startValue=doubled
        #     else:
        #         startValue=substracted
        #     cnt+=1
        # return cnt
                
       ###start from target
       cnt=0
       while target>startValue:
            if target%2==0:
                target//=2
            else:
                target+=1
            cnt+=1
       return cnt+(startValue-target)

        