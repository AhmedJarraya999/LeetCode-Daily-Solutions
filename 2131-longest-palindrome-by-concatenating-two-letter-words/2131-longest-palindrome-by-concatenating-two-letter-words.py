from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        total_len = 0
        has_center = False

        for word in count:
            rev = word[::-1]
            if word != rev:
                if word < rev:  # Avoid double counting
                    pair_count = min(count[word], count[rev])
                    total_len += pair_count * 4
            else:
                # word is like "gg", "aa"
                pair_count = count[word] // 2
                total_len += pair_count * 4
                if count[word] % 2 == 1:
                    has_center = True

        if has_center:
            total_len += 2

        return total_len
