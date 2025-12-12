class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows=defaultdict(lambda:[n,0])
        cols=defaultdict(lambda:[n,0])
        for r,c in buildings:
            rows[r][0]=min(rows[r][0],c)
            rows[r][1]=max(rows[r][1],c)

            cols[c][0]=min(cols[c][0],r)
            cols[c][1]=max(cols[c][1],r)
        res=0
        for r,c in buildings:
            if rows[r][0]<c<rows[r][-1] and cols[c][0]<r<cols[c][-1]:
                res+=1
        return res





        res=0
        myset=set()
        for x,y in buildings:
            myset.add((x,y))
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        building_x_sorted=sorted(buildings,key=lambda b: b[0])
        # x_surrounedd_checker=[float('inf') for _ in range(n)]
        # y_surrounded_checker=[float('inf') for _ in range(n)]
        building_y_sorted=sorted(buildings,key=lambda b:b[1])
        for x,y in buildings:
            if (x>0) and (x<n-1) and (y>0) and (y<n-1):
                if x!=building_x_sorted[0] and x!=building_x_sorted[n-1] and y!=building_y_sorted[0] and y!=building_y_sorted[n-1]:
                    res+=1
            # up=any((i,y) in myset for i in range(1,x))
            # down=any((i,y) in myset for i in range(x+1,n+1))
            # left=any((x,j) in myset for j in range(1,y))
            # right=any((x,j) in myset for j in range(y+1,n+1))
            # if up and down and right and left:
            #     res+=1
        return res


        #CLEANER
        # for x, y in buildings:
        #     if all((x + dx, y + dy) in myset for dx, dy in directions):
        #         res += 1
        
        # return res



        # for x,y in buildings:
        #     all_in_set = True
        #     for dx, dy in directions:
        #         nx, ny = x + dx, y + dy
        #         if 0<=nx<n and 0<=ny<n:
        #             if (nx,ny) not in myset:
        #                 all_in_set = False
        #                 break
        #         else:
        #             all_in_set = False
        #             break
        #     if all_in_set:
        #         res+=1 
        # return res





        