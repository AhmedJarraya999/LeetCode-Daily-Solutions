class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        res=0
        myset=set(brokenLetters)
        
        for word in text.split():
            valid=True
            for c in word:
                if c in myset:
                    valid=False
                    break
            if valid:
                res+=1
        return res
        
                
        