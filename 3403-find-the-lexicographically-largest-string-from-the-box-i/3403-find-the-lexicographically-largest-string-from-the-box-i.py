class Solution:
        def answerString(self, word: str, numFriends: int) -> str:
            n=len(word)
            l=n-(numFriends-1)
            if numFriends==1:
                return word
            best=""
            for i in range(n):
                if word[i:i+l]>best:
                    best=word[i:i+l]
            return best  
            