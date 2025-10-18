class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # used=set()
        # for num in nums:
        #     for val in range (num-k,num+k+1):
        #         if val not in used:
        #             used.add(val)
        #             break
        # return len(used)
        nums.sort()
        next_available = float('-inf')
        count = 0
        
        for num in nums:
            # The smallest value we can assign to this number
            low = num - k
            high = num + k
            
            # Ensure we start at least from the next available
            if next_available < low:
                next_available = low
                
            # If we can assign a value in the range
            if next_available <= high:
                count += 1
                next_available += 1  # move to the next unused number
                
        return count


        