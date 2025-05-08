class Solution(object):
    def longestSemiRepetitiveSubstring(self, s):
        l = 0
        tracker = 0
        res = 0
        for r in range(len(s)):
            if r > 0 and s[r] == s[r - 1]:
                tracker += 1
            while tracker > 1:
                if s[l] == s[l + 1]:
                    tracker -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
