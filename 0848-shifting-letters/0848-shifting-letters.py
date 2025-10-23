class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        total_shift = 0
        res = [''] * n

        # Compute cumulative shifts from the end
        for i in reversed(range(n)):
            total_shift = (total_shift + shifts[i]) % 26
            # Shift the character
            res[i] = chr((ord(s[i]) - ord('a') + total_shift) % 26 + ord('a'))

        return ''.join(res)