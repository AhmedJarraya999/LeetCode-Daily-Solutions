class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def backtrack(i,curSum):
            if curSum==n:
                return True
            if curSum>n or 3**i>n:
                return False
            #include
            if  backtrack(i+1,curSum+3**i):
                return True
            return backtrack(i+1,curSum)
        return backtrack(0,0)
            

        
