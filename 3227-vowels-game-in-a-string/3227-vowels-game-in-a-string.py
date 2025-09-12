class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        # Count vowels
        vowel_count = sum(1 for c in s if c in vowels)
        # Alice wins if there is at least one vowel
        return vowel_count > 0
