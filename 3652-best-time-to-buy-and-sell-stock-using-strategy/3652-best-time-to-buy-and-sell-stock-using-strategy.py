class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n=len(prices)
        prefix_price=[0]*(n+1)
        prefix_old=[0]*(n+1)
        for i in range(n):
            prefix_price[i + 1] = prefix_price[i] + prices[i]
            prefix_old[i + 1] = prefix_old[i] + prices[i] * strategy[i]
        base_profit=sum(prices[i]*strategy[i] for i in range(n))
        max_profit=base_profit
        for start in range(n-k+1): #o(n**2)
            mid=start+k//2
            end=start+k
            old_window=prefix_old[end]-prefix_old[start]
            new_window=prefix_price[end]-prefix_price[mid]
            profit=base_profit-old_window+new_window
            max_profit=max(profit,max_profit)
        return max_profit 

        #bf
            # tmp_strategy=strategy.copy()
            # for i in rang(k/2):
            #     tmp_strategy[start+i]=0
            # for i in range(k/2,k):
            #     temp_strategy[start+i]=1
            # cur_prof=sum(price[i]*tmp_strategy[i]) for i in range(n)
            # best=max(best,cur_prof)
        #bf
        # return best 


            





        # n = len(prices)

        # # 1. Original profit
        # base_profit = sum(p * s for p, s in zip(prices, strategy))

        # # 2. Prefix sums for prices and strategy * prices
        # prefix_price = [0] * (n + 1)
        # prefix_old = [0] * (n + 1)

        # for i in range(n):
        #     prefix_price[i + 1] = prefix_price[i] + prices[i]
        #     prefix_old[i + 1] = prefix_old[i] + prices[i] * strategy[i]

        # max_profit = base_profit
        # half = k // 2

        # # 3. Slide window
        # for start in range(n - k + 1):
        #     mid = start + half
        #     end = start + k
        #     # Old contribution of the window
        #     old_window = prefix_old[end] - prefix_old[start]

        # # New contribution:
        # # first half -> 0
        # # second half -> sell (1)
        #     new_window = prefix_price[end] - prefix_price[mid]

        # # New total profit
        #     new_profit = base_profit - old_window + new_window
        #     max_profit = max(max_profit, new_profit)
        # return max_profit

        #####BF#########
        # n=len(prices)
        # def prof(s):
        #     return sum(p*a for p,a in zip(prices,s))
        # res=sum(p*a for p,a in zip(prices,strategy))
        # for start in range(n-k+1):
        #     temp_strategy=strategy.copy()
        #     for i in range(k//2):
        #         temp_strategy[start+i]=0
        #     for i in range(k//2,k):
        #         temp_strategy[start+i]=1
        #     current_profit = prof(temp_strategy)
        #     res=max(current_profit,res)
        # return res
        

        