from collections import defaultdict

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        n += 1
        while True:
            count_map = defaultdict(int)
            for x in str(n):
                count_map[int(x)] += 1
            
    
            valid = True
            for digit, count in count_map.items():
                if digit != count:
                    valid = False
                    break
            
            if valid:
                return n
            n += 1
