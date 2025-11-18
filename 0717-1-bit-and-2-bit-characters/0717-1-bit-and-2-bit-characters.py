class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        n = len(bits)

        while i < n - 1:
            if bits[i] == 1:
                i += 2   # two-bit character
            else:
                i += 1   # one-bit character

        # If we stopped exactly on the last index, it's a 0 (one-bit)
        return i == n - 1
