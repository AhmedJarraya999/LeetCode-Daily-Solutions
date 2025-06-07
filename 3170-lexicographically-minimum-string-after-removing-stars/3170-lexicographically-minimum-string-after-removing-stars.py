class Solution:
    def clearStars(self, s: str) -> str:
        from collections import deque

        stack = []

        for ch in s:
            if ch != '*':
                stack.append(ch)
            else:
                # Find the smallest character in stack
                min_char = min(stack)
                # Remove rightmost occurrence of that smallest character
                for i in range(len(stack) - 1, -1, -1):
                    if stack[i] == min_char:
                        del stack[i]
                        break

        return ''.join(stack)

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
        