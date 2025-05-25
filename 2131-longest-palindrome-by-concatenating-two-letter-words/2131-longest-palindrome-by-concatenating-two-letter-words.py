class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        def helper(word1, word2):
            both=word1+word2
            def is_palindrom(s,left,right):
                if left>=right:
                    return True
                if s[left]!=s[right]:
                    return False
                return is_palindrom(s,left+1,right-1)
            return is_palindrom(both,0,len(both)-1)

        n = len(words)
        used = [False] * n
        total_len = 0
        center_used = False

        for i in range(n):
            if used[i]:
                continue
            for j in range(i + 1, n):
                if not used[j] and helper(words[i], words[j]):
                    total_len += 4
                    used[i] = True
                    used[j] = True
                    break

        
        for i in range(n):
            if not used[i] and words[i][0] == words[i][1]:
                total_len += 2
                break

        return total_len



        

        