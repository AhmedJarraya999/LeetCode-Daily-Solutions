class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cond1 = word.isupper()          
        cond2 = word.islower()           
        cond3 = word[0].isupper() and word[1:].islower()  
        return cond1 or cond2 or cond3
        