class Solution:
    def countSubsequences(self, s: str, next_str: str) -> int:
        i = 0  # Index in s
        j = 0  # Index in next_str
        m = len(next_str)
        subsequence_count = 0

        while i < len(s):
            if s[i] == next_str[j]:
                j += 1
                if j == m:
                    j = 0
                    subsequence_count += 1
            i += 1
        return subsequence_count

    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        n = len(s)
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        # BFS
        curr = ""
        queue = deque()
        queue.append(curr)
        res = ""

        while queue:
            curr = queue.popleft()
            
            for c in range(ord('a'), ord('z') + 1):
                char = chr(c)
                if freq[c - ord('a')] < k:
                    continue
                next_str = curr + char
                if self.countSubsequences(s, next_str) >= k:
                    res = next_str
                    queue.append(next_str)
        return res