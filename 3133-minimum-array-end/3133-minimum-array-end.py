import math

class Solution:
    def getBin(self, n):
        res = []
        while n:
            res.append(1 if (n & 1) else 0)
            n >>= 1
        return res

    def minEnd(self, n, x):
        if n == 1:
            return x

        # Step-1: Record zero positions
        zero_pos = []
        count = 0
        val = x
        while val:
            if (val & 1) == 0:
                zero_pos.append(count)
            count += 1
            val >>= 1

        # Step-2: Find the number of bits required to make N combinations
        reqd_bits = math.ceil(math.log2(n))

        # Step-3: Append more bits in zero_pos as per requirement
        zero_pos.extend(range(count, count + (reqd_bits - len(zero_pos))))
        
        # Step-4: Find bits to be appended
        append_bits = self.getBin(n - 1)

        # Step-5: Form the answer
        ans = x
        pos = len(append_bits)
        while pos:
            pos -= 1
            if append_bits[pos] == 1:
                ans += (1 << zero_pos[pos])

        return ans