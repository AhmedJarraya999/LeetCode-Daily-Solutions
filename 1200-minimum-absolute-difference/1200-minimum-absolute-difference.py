class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res=[]
        arr.sort()
        min_abs_diff=float('inf')
        for i in range(1,len(arr)):
            min_abs_diff=min(abs(arr[i]-arr[i-1]),min_abs_diff)
        for i in range(1,len(arr)):
            if abs(arr[i]-arr[i-1])==min_abs_diff:
                res.append((arr[i-1],arr[i]))
        return res


        