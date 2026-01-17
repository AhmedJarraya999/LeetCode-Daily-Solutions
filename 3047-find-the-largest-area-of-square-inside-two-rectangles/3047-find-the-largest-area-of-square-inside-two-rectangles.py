class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        overlappings=[]
        n=len(bottomLeft)
        for i in range(n):
            for j in range(i+1,n):
                x_left   = max(bottomLeft[i][0], bottomLeft[j][0])
                y_bottom = max(bottomLeft[i][1], bottomLeft[j][1])
                x_right  = min(topRight[i][0], topRight[j][0])
                y_top    = min(topRight[i][1], topRight[j][1])
                if x_right > x_left and y_top > y_bottom:
                    overlappings.append([[x_left, y_bottom], [x_right, y_top]])
        max_square = 0
        for rect in overlappings:
            width  = rect[1][0] - rect[0][0]
            height = rect[1][1] - rect[0][1]
            side = min(width, height)
            max_square = max(max_square, side * side)
        return max_square
        


        