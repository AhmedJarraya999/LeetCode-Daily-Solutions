class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        # next_zero[i] = index of the next zero after i (i exclusive),
        # or n if none exists
        next_zero = [n] * n
        for i in range(n - 2, -1, -1):
            if s[i + 1] == '0':
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i + 1]

        res = 0

        # For each left index L, grow the substring zero-by-zero
        for L in range(n):
            zeros = 1 if s[L] == '0' else 0
            R = L

            # only need to try until zeros^2 <= n (since zeros^2 grows fast)
            while zeros * zeros <= n:
                next_z = next_zero[R] if R < n else n

                # minimal end index E_min that satisfies:
                # ones_in_sub = (E - L + 1) - zeros >= zeros^2
                # -> E >= L + zeros^2 + zeros - 1
                E_min = L + zeros * zeros + zeros - 1

                # earliest endpoint we can actually use in this block:
                start = max(R, E_min)

                # count endpoints in [start .. next_z-1]
                if start <= next_z - 1:
                    res += (next_z - start)

                # move R to the next zero and include that zero
                R = next_z
                if R >= n:
                    break
                zeros += 1

        return res