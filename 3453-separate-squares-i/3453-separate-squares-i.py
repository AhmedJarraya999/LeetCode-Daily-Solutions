class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def calculate_area(mid):
            top=0
            bottom=0
            for x,y,l in squares:
                top_limit=y+l
                bottom_limit=y
                #elmid yeksem el rectangle l zouz 
                if bottom_limit<=mid<=top_limit:
                    top+=(top_limit-mid)*l
                    bottom+=(mid-bottom_limit)*l
                elif mid<bottom_limit:
                    top+=l*l
                elif mid>top_limit:
                    bottom+=l*l
            return top-bottom
        miny = float('inf')
        maxy = float('-inf')
        #initial boundaries
        for x, y, l in squares:
            miny = min(miny, y)
            maxy = max(maxy, y + l)
        #initialise binary search
        left, right = miny, maxy
        eps = 1e-6
        while right - left > eps:
            mid=(left+right)/2
            diff=calculate_area(mid)
            if diff>0:
                left=mid
            else:
                right=mid
        return (left + right) / 2








