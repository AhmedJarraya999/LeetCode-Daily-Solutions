class Solution:
    def maxDifference(self, s: str) -> int:
        freq=Counter(s)
        odd_freq=[]
        even_freq=[]
        max_odd=float('-inf')
        min_even=float('inf')
        for count in freq.values():
            if count%2==1: 
                if count>max_odd:
                    max_odd=count
            else: 
                if count<min_even:
                    min_even=count
        if max_odd == float('-inf') or min_even == float('inf'):
            return 0
        return  max_odd-min_even
                   



        