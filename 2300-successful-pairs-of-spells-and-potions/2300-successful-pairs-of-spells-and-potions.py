import bisect

class Solution:
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        m = len(potions)
        result = []

        for s in spells:
            # Minimum potion strength required
            min_strength = (success + s - 1) // s  # ceiling division
            # Find the index using binary search
            idx = bisect.bisect_left(potions, min_strength)
            # Count how many potions from idx to end are successful
            result.append(m - idx)

        return result
