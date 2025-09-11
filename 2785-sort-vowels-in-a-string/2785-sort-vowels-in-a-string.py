class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = set("AEIOUaeiou")
        
        # Extract vowels and sort them
        sorted_vowels = sorted([ch for ch in s if ch in vowels])
        
        # Iterator for sorted vowels
        it = iter(sorted_vowels)
        
        # Rebuild the string: replace vowels with sorted ones
        result = []
        for ch in s:
            if ch in vowels:
                result.append(next(it))
            else:
                result.append(ch)
        
        return "".join(result)
