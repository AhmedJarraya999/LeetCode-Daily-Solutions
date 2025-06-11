class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def get_status(a, b):
            return ((a & 1) << 1) | (b & 1)

        n = len(s)
        ans = float('-inf')

        for ca in range(5):
            for cb in range(5):
                if ca == cb:
                    continue
                best = [float('inf')] * 4
                cnt_a = cnt_b = prev_a = prev_b = 0
                left = -1
                for right in range(n):
                    cnt_a += (s[right] == str(ca))
                    cnt_b += (s[right] == str(cb))

                    while right - left >= k and cnt_b - prev_b >= 2:
                        status = get_status(prev_a, prev_b)
                        best[status] = min(best[status], prev_a - prev_b)
                        left += 1
                        prev_a += (s[left] == str(ca))
                        prev_b += (s[left] == str(cb))

                    status = get_status(cnt_a, cnt_b)
                    if best[status ^ 2] < float('inf'):
                        ans = max(ans, (cnt_a - cnt_b) - best[status ^ 2])

        return ans if ans != float('-inf') else -1
