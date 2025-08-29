class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        oddX,evenX=(n+1)//2,n//2
        oddY, evenY = (m + 1) // 2, m // 2
        return oddX * evenY + evenX * oddY
        #O(n*m)
        # count=0
        # for x in range(1,n+1):
        #     for y in range(1,m+1):
        #         if (x+y)%2==1:
        #             count+=1
        # return count
        