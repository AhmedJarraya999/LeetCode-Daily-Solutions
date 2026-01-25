import heapq

class Node:
    def __init__(self, val, i):
        self.val = val
        self.i = i
        self.prev = None
        self.next = None
        self.alive = True

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        # Create doubly linked list
        head = Node(nums[0], 0)
        cur = head
        nodes = [head]
        for i in range(1, len(nums)):
            node = Node(nums[i], i)
            node.prev = cur
            cur.next = node
            cur = node
            nodes.append(node)

        heap = []
        inversions = 0
        
        # Count initial inversions and fill the heap
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                inversions += 1
            heapq.heappush(heap, (nums[i] + nums[i-1], i-1, nodes[i-1]))

        ops = 0

        # Process until no inversions remain
        while inversions:
            while heap:
                tot, i, left = heapq.heappop(heap)
                right = left.next

                # Skip invalid nodes
                if not left.alive or not right or not right.alive:
                    continue
                if left.val + right.val != tot:
                    continue
                break
            else:
                # Heap is empty but inversions > 0 -> prevent infinite loop
                break

            # Remove inversions caused by this pair before update
            if left.prev and left.val < left.prev.val:
                inversions -= 1
            if left.next and left.val > left.next.val:
                inversions -= 1

            # Merge left and right
            left.val = tot
            right.alive = False
            left.next = right.next
            if right.next:
                right.next.prev = left

            # Count new inversions after merge
            if left.prev and left.val < left.prev.val:
                inversions += 1
            if left.next and left.val > left.next.val:
                inversions += 1

            # Add new possible pairs to heap
            if left.prev:
                heapq.heappush(heap, (left.prev.val + left.val, left.prev.i, left.prev))
            if left.next:
                heapq.heappush(heap, (left.val + left.next.val, left.i, left))

            ops += 1

        return ops
