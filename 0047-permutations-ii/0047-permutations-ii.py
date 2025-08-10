class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm=[]
        res=[]
        count=defaultdict(int)
        for num in nums:
            count[num]+=1
        def dfs():
            if len(perm)==len(nums):
                res.append(perm.copy())
                return
            for n in count:
                if count[n]>0:
                    perm.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    perm.pop()
        dfs()
        return res


        
        