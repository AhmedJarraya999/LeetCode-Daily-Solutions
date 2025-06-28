class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums=list(enumerate(nums))
        #sort by valued decending pick top k
        top_k=sorted(indexed_nums,key=lambda x:x[1],reverse=True)[:k]
        #sort top_k  based on index now
        top_k_sorted=sorted(top_k,key=lambda x:x[0])
        return [num for idx,num in top_k_sorted]
        
        