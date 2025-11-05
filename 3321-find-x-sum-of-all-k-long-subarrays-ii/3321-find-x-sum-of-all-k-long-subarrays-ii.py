from collections import Counter
import heapq

class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        freq = Counter(nums[:k])

        # Helper key: element compared by (freq, value).
        # topHeap: min-heap by (freq, val, num) for the x best elements
        # restHeap: max-heap via (-freq, -val, num) for others
        topHeap = []
        restHeap = []
        in_top = set()
        sumTop = 0

        # Build initial top-x by sorting once (only at start)
        items = list(freq.items())  # (num, freq)
        items.sort(key=lambda p: (-p[1], -p[0]))  # best first by freq desc, value desc
        for idx, (num, f) in enumerate(items):
            if idx < x:
                in_top.add(num)
                sumTop += num * f
                heapq.heappush(topHeap, (f, num, num))  # (freq, val, num)
            else:
                heapq.heappush(restHeap, (-f, -num, num))

        def clean_top():
            # remove invalid entries from topHeap's top
            while topHeap:
                f, val, num = topHeap[0]
                # valid only if freq matches and num in in_top
                if freq.get(num, 0) != f or num not in in_top:
                    heapq.heappop(topHeap)
                else:
                    break

        def clean_rest():
            # remove invalid entries from restHeap's top
            while restHeap:
                nf, nval, num = restHeap[0]
                # stored as (-freq, -val)
                if freq.get(num, 0) != -nf or (num in in_top):
                    heapq.heappop(restHeap)
                else:
                    break

        def maybe_promote():
            # Promote best from rest to top while we have < x elements
            nonlocal sumTop
            clean_rest()
            while len(in_top) < x and restHeap:
                nf, nval, num = heapq.heappop(restHeap)
                f = -nf
                # skip if freq changed or now in_top
                if freq.get(num, 0) != f or num in in_top:
                    clean_rest()
                    continue
                in_top.add(num)
                sumTop += num * f
                heapq.heappush(topHeap, (f, num, num))
                clean_rest()

        def maybe_demote():
            # Demote smallest in top while we have > x elements
            nonlocal sumTop
            clean_top()
            while len(in_top) > x:
                f, val, num = heapq.heappop(topHeap)
                # skip outdated
                if freq.get(num, 0) != f or num not in in_top:
                    clean_top()
                    continue
                # demote it
                in_top.remove(num)
                sumTop -= num * f
                heapq.heappush(restHeap, (-f, -num, num))
                clean_top()

        def swap_if_needed():
            # If best in rest is better than worst in top, swap them.
            nonlocal sumTop
            clean_top(); clean_rest()
            while topHeap and restHeap:
                f_top, val_top, num_top = topHeap[0]
                nf_rest, nval_rest, num_rest = restHeap[0]
                f_rest = -nf_rest
                val_rest = -nval_rest
                # Compare (freq, val) pairs
                if (f_rest > f_top) or (f_rest == f_top and val_rest > val_top):
                    # pop both (validity checked in clean_*), swap membership
                    heapq.heappop(topHeap)
                    heapq.heappop(restHeap)
                    # remove top
                    in_top.remove(num_top)
                    sumTop -= num_top * f_top
                    heapq.heappush(restHeap, (-f_top, -num_top, num_top))
                    # add rest into top
                    in_top.add(num_rest)
                    sumTop += num_rest * f_rest
                    heapq.heappush(topHeap, (f_rest, num_rest, num_rest))
                    clean_top(); clean_rest()
                else:
                    break

        # Ensure initial sizes consistent
        maybe_promote()
        maybe_demote()
        swap_if_needed()

        ans = [sumTop]

        # Slide window
        for i in range(k, n):
            left = nums[i - k]
            right = nums[i]

            # handle left removal
            old_f = freq.get(left, 0)
            if old_f > 0:
                # if left was in_top, adjust sumTop by removing old contribution then add new one
                if left in in_top:
                    sumTop -= left * old_f
                new_f = old_f - 1
                if new_f == 0:
                    freq.pop(left, None)
                else:
                    freq[left] = new_f
                # push updated tuple lazily into appropriate heap
                if left in in_top:
                    # push new tuple to topHeap (if still in_top, we'll check when cleaning)
                    if new_f > 0:
                        heapq.heappush(topHeap, (new_f, left, left))
                    else:
                        # fully removed: demote if it was in_top
                        in_top.discard(left)
                else:
                    if new_f > 0:
                        heapq.heappush(restHeap, (-new_f, -left, left))
                # if left still in_top after freq decrement, add its new contribution
                if left in in_top and new_f > 0:
                    sumTop += left * new_f

            # handle right addition
            old_f_r = freq.get(right, 0)
            new_f_r = old_f_r + 1
            freq[right] = new_f_r
            # update sumTop if right was in_top (it may or may not)
            if right in in_top:
                # remove old contribution then add updated
                sumTop -= right * old_f_r
                sumTop += right * new_f_r
                heapq.heappush(topHeap, (new_f_r, right, right))
            else:
                # push to rest; it may be promoted later
                heapq.heappush(restHeap, (-new_f_r, -right, right))

            # Rebalance sizes and membership
            maybe_promote()
            maybe_demote()
            swap_if_needed()

            ans.append(sumTop)

        return ans
