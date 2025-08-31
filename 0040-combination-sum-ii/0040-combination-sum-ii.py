class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def backtrack(start,path,cumsum):
            if cumsum==target:
                res.append(path[:])
                return
            if cumsum>target:
                return 
            for i in range(start, len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                backtrack(i+1,path,cumsum+candidates[i])
                path.pop()
        backtrack(0,[],0)
        return res