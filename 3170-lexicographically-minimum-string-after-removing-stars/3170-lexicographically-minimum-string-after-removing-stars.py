import heapq
from collections import defaultdict

class Solution:
    def clearStars(self, s: str) -> str:
        stack = []
        heap = []
        char_pos = defaultdict(list)
        deleted = set()  # indices in stack that are deleted

        for ch in s:
            if ch != '*':
                idx = len(stack)
                stack.append(ch)
                char_pos[ch].append(idx)
                heapq.heappush(heap, ch)
            else:
                # Remove the smallest valid character
                while heap:
                    min_char = heapq.heappop(heap)
                    if char_pos[min_char]:
                        break  # found the valid smallest char
                
                # Remove the last occurrence of min_char
                del_idx = char_pos[min_char].pop()
                deleted.add(del_idx)

        # Reconstruct the string excluding deleted indices
        result = []
        for i, ch in enumerate(stack):
            if i not in deleted:
                result.append(ch)
        
        return ''.join(result)

        #TLE SOLUTION
        # stack=[]
        # for ch in s:
        #     if ch!='*':
        #         stack.append(ch)
        #     else: 
        #         if stack:
        #             min_char=min(stack)
        #             for i in range(len(stack)-1,-1,-1):
        #                 if stack[i]==min_char:
        #                     del stack[i]
        #                     break 
        # return ''.join(stack)
        