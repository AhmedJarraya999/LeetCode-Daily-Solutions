class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1

        # Calculate the number of bits needed
        num = k
        bits = 0
        while num:
            num //= 2
            bits += 1

        res = 0
        for i in range(bits):
            if (k >> i) & 1:
                res += operations[i]

        return chr(ord('a') + (res % 26))
