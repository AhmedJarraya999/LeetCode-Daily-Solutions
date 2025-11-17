class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack=[]
        n=len(prices)
        res=prices[:]
        for i in range(n-1,-1,-1):
            # pop all prices greater than the current price
            while stack and stack[-1]>prices[i]:
                stack.pop()
            # if stack has an element, it is the discount
            if stack:
                res[i] -= stack[-1]
            # push current price for future elements
            stack.append(prices[i])
        return res