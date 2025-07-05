class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter=Counter(arr)
        res=-1
        for num,freq in counter.items():
            if freq==num:
                res=max(res,freq)
        return res
        