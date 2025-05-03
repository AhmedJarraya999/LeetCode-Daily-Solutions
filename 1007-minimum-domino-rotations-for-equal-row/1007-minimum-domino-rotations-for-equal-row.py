class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        def check(x):
            missingT=0
            missingB=0
            #zip tparcouri 2 arrays simulatenously
            for i,(top,bottom) in enumerate(zip(tops,bottoms)):
                if not(top==x or bottom==x):
                    return -1
                if top!=x:
                    missingT+=1
                if bottom!=x:
                    missingB+=1
                if i==len(tops)-1:
                    return min(missingT,missingB)
        res1=check(tops[0])
        res2=check(bottoms[0])
        if res1==-1 and res2==-1:
            return -1
        elif res1==-1:
            return res2
        elif res2==-1:
            return res1
        else:
            return min(res1,res2)
















        t1 = tops[0]
        missingT = 0
        missingB = 0
        for i, (top, bottom) in enumerate(zip(tops, bottoms)):
            if not (top == t1 or bottom == t1):
                return -1
            if top != t1:
                missingT += 1
            if bottom != t1:
                missingB += 1
            if i == len(tops) - 1:
                return min(missingT, missingB)
