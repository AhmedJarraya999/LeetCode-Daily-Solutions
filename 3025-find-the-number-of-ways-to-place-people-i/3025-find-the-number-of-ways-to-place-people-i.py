class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n=len(points)
        count=0
        for i in range(n):
            for j in range(n):
                if i==j:
                    continue
                ax,ay=points[i]
                bx,by=points[j]
                if ax<=bx and ay>=by and not (ax == bx and ay == by):
                    works=True
                    for x in range(n):
                        if x==i or x==j:
                            continue
                        cx,cy=points[x]
                        if ax<=cx<=bx and by<=cy<=ay and not(cx==bx and cy==by):
                            works=False
                            break
                    if works:
                        count+=1
        return count

        