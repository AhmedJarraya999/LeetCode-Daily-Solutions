class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mod_map=defaultdict(int)
        for num in nums:
                mod_map[num % value] += 1
        # total = sum(mod_map.values())
        i=0
        while True:
            remainder=i%value
            if mod_map[remainder]>0:
                mod_map[remainder]-=1
                i+=1
            else:
                return i
        
        

        