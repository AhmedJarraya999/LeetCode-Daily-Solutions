class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n=len(cardPoints)
        if k==n:
            return sum(cardPoints)
        total=sum(cardPoints)
        window_size=n-k
        window_sum=sum(cardPoints[:window_size])
        min_window=window_sum
        for i in range(window_size,n):
            window_sum+=cardPoints[i]
            window_sum-=cardPoints[i-window_size]
            min_window=min(min_window,window_sum)
        return total-min_window
      
            
        

        