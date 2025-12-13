from typing import List
import re

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        valid_lines = ["electronics", "grocery", "pharmacy", "restaurant"]
        
        # Prepare buckets for sorting by business line order
        buckets = {line: [] for line in valid_lines}
        
        for c, b, active in zip(code, businessLine, isActive):
            # Condition 1: active
            if not active:
                continue
            
            # Condition 2: valid business line
            if b not in valid_lines:
                continue
            
            # Condition 3: valid code (non-empty, alphanumeric + _)
            if not c or not re.fullmatch(r"[A-Za-z0-9_]+", c):
                continue
            
            buckets[b].append(c)
        
        # Sort codes inside each business line
        result = []
        for line in valid_lines:
            result.extend(sorted(buckets[line]))
        
        return result
