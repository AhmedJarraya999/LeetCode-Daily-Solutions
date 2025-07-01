class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #bottom up dp
        dp = [float('inf')] * (amount + 1)
        dp[0]=0
        for c in coins:
            for i in range(c,amount+1):
                dp[i]=min(dp[i],dp[i-c]+1)
        return dp[amount] if dp[amount] != float('inf') else -1
        #=========>>>>backtracking solution
        # result = [float('inf')] 
        # def backtrack(remain,count):
        #     if remain==0:
        #         result[0]=min(result[0],count)
        #     if remain<0:
        #         return
        #     for coin in coins:
        #         backtrack(remain-coin,count+1)
        # backtrack(amount,0)
        # return result[0] if result[0]!=float('inf') else -1


        