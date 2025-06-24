class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_indices=[]
        res=set()
        for i in range(len(nums)):
            if nums[i]==key:
                key_indices.append(i)
        for j in key_indices:
            for i in range(max(0,j-k),min(len(nums),j+k+1)):
                res.add(i)
        res=sorted(res)
        return res
    
        
            

            
        