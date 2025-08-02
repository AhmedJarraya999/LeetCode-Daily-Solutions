from collections import Counter

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)
        total = count1 + count2
        
        # Check if we can make them equal
        for fruit, freq in total.items():
            if freq % 2 != 0:
                return -1

        # Compute how many of each fruit we need to swap from basket1
        to_swap = []
        for fruit in total:
            diff = count1[fruit] - count2[fruit]
            if diff > 0:
                to_swap.extend([fruit] * (diff // 2))
            elif diff < 0:
                to_swap.extend([fruit] * ((-diff) // 2))
        
        to_swap.sort()
        min_fruit = min(total)

        # Only half the swaps are needed, because we're pairing one from basket1 with one from basket2
        swaps_needed = len(to_swap) // 2
        cost = 0
        for i in range(swaps_needed):
            cost += min(to_swap[i], 2 * min_fruit)
        return cost
