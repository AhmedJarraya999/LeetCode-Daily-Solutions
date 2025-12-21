# class Solution:
#     def minDeletionSize(self, strs: List[str]) -> int:
#         from itertools import combinations
#         def is_sorted(arr):
#             for i in range(len(arr)-1):
#                 if arr[i]>arr[i+1]:
#                     return False
#             return True
#         rows=len(strs)
#         cols=len(strs[0])
#         ans=cols
#         for k in range(cols+1):#nb  of deleted columns
#             for deleted in combinations(range(cols),k):
#                 new_strs=[]
#                 for s in strs:
#                     new_s=""
#                     for i in range(cols):
#                         if i not in deleted:
#                             new_s+=s[i]
#                     new_strs.append(new_s)
#                 if is_sorted(new_strs):
#                     return k
#         return ans
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows = len(strs)
        cols = len(strs[0])

        deleted = 0
        sorted_pairs = [False] * (rows - 1)

        for c in range(cols):
            # Check if this column is bad
            bad = False
            for r in range(rows - 1):
                if not sorted_pairs[r] and strs[r][c] > strs[r + 1][c]:
                    bad = True
                    break

            if bad:
                deleted += 1
                continue

            # Update which pairs are now sorted
            for r in range(rows - 1):
                if strs[r][c] < strs[r + 1][c]:
                    sorted_pairs[r] = True

        return deleted




        