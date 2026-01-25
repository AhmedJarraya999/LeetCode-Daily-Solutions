import heapq
from typing import List

class Node:
    def __init__(self, val: int, i: int):
        self.val = val
        self.prev = None
        self.next = None
        self.alive = True   # for lazy deletion
        self.i = i


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)

        # build doubly linked list
        dll = Node(nums[0], 0)
        curr = dll
        nodes = [dll]

        for i in range(1, n):
            node = Node(nums[i], i)
            curr.next = node
            node.prev = curr
            curr = node
            nodes.append(node)

        inversions = 0
        heap = []

        # count initial inversions and push adjacent pairs
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                inversions += 1
            heapq.heappush(heap, (nums[i] + nums[i - 1], i - 1, nodes[i].prev))

        ops = 0
        while inversions:
            # lazy deletion loop
            while True:
                total, i, left = heapq.heappop(heap)
                right = left.next
                if not left.alive or not right or not right.alive:
                    continue
                if left.val + right.val != total:
                    continue
                break

            # remove left-right related inversions
            if left.prev and left.val < left.prev.val:
                inversions -= 1
            if right.val < left.val:
                inversions -= 1
            if right.next and right.next.val < right.val:
                inversions -= 1

            # merge right into left
            left.val = total
            right.alive = False
            left.next = right.next
            if right.next:
                right.next.prev = left

            # add new possible inversions
            if left.prev and left.val < left.prev.val:
                inversions += 1
            if left.next and left.next.val < left.val:
                inversions += 1

            # push new adjacent pairs
            if left.prev:
                heapq.heappush(
                    heap,
                    (left.prev.val + left.val, left.prev.i, left.prev)
                )
            if left.next:
                heapq.heappush(
                    heap,
                    (left.val + left.next.val, left.i, left)
                )

            ops += 1

        return ops
