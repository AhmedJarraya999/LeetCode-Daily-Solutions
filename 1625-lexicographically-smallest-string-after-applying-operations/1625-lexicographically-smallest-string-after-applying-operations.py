from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        visited = set()
        queue = deque([s])
        smallest = s

        while queue:
            cur = queue.popleft()
            if cur in visited:
                continue
            visited.add(cur)

            # Update smallest string if needed
            if cur < smallest:
                smallest = cur

            # Operation 1: add 'a' to all odd indices
            chars = list(cur)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            added = ''.join(chars)

            # Operation 2: rotate right by b
            rotated = cur[-b:] + cur[:-b]

            # Enqueue next states
            if added not in visited:
                queue.append(added)
            if rotated not in visited:
                queue.append(rotated)

        return smallest
