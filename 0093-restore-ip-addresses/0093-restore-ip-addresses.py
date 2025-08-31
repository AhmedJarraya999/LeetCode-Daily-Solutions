from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, parts):
            if len(parts) == 4 and start == len(s):
                res.append(".".join(parts))
                return
            if len(parts) >= 4:
                return
            for length in range(1, 4):
                if start + length > len(s):
                    break
                segment = s[start:start+length]
                if (segment.startswith("0") and len(segment) > 1) or int(segment) > 255:
                    continue
                parts.append(segment)
                backtrack(start + length, parts)
                parts.pop()

        backtrack(0, [])
        return res
