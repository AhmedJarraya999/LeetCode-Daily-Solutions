class Solution(object):
    def getLongestSubsequence(self, words, groups):
        result=[]
        prev_group=-1
        for word, group in zip(words, groups):
            if group!=prev_group:
                result.append(word)
                prev_group=group
        return result
            

        