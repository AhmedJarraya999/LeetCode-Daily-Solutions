class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter=Counter(nums)
        return [num for num,freq in heapq.nlargest(k,counter.items(),key=lambda x:x[1])]
        