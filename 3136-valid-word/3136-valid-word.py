class Solution:
    def isValid(self, word: str) -> bool:
        if len(word)<3:
            return False
        if not word.isalnum():
            return False
        vowels=set('aeiouAEIOU')
        has_vowel=False
        has_consolnant=False
        for char in word:
            if char.isalpha():
                if char in vowels:
                    has_vowel=True
                else:
                    has_consolnant=True
        return has_vowel and has_consolnant



        