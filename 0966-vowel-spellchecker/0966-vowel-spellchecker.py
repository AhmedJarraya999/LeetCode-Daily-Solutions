from typing import List

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        words = set(wordlist)  # for exact match
        
        # Case insensitive map (store first occurrence)
        lower_map = {}
        # Vowel error map (replace vowels with "*")
        vowel_map = {}

        def devowel(word: str) -> str:
            vowels = set("aeiou")
            return "".join('*' if ch in vowels else ch for ch in word)

        for word in wordlist:
            lower = word.lower()
            if lower not in lower_map:
                lower_map[lower] = word
            dv = devowel(lower)
            if dv not in vowel_map:
                vowel_map[dv] = word

        result = []
        for q in queries:
            if q in words:  # exact match
                result.append(q)
            elif q.lower() in lower_map:  # case-insensitive match
                result.append(lower_map[q.lower()])
            elif devowel(q.lower()) in vowel_map:  # vowel error match
                result.append(vowel_map[devowel(q.lower())])
            else:
                result.append("")  # no match
        return result
