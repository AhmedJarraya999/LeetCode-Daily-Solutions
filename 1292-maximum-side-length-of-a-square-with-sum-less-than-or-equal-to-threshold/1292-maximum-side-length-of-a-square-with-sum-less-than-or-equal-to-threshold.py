class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        # Prefix sum
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = (
                    mat[i - 1][j - 1]
                    + prefix[i - 1][j]
                    + prefix[i][j - 1]
                    - prefix[i - 1][j - 1]
                )

        def exists(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    total = (
                        prefix[i + k][j + k]
                        - prefix[i][j + k]
                        - prefix[i + k][j]
                        + prefix[i][j]
                    )
                    if total <= threshold:
                        return True
            return False

        left, right = 0, min(m, n)
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
