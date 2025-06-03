class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n = len(status)
        visited = [False] * n
        has_key = [False] * n
        queue = deque(initialBoxes)
        total_candies = 0
        
        while queue:
            size = len(queue)
            progress = False  #Reset progress inside the loop
            for _ in range(size):
                box = queue.popleft()
                if visited[box]:
                    continue
                if status[box] == 1 or has_key[box]:
                    progress = True
                    visited[box] = True
                    total_candies += candies[box]
                    
                    # Collect keys
                    for key in keys[box]:
                        has_key[key] = True
                        if not visited[key]:
                            queue.append(key)
                    
                    # Collect contained boxes
                    for contained in containedBoxes[box]:
                        queue.append(contained)
                else:
                    # Can't open it yet
                    queue.append(box)
            
            if not progress:
                break
        
        return total_candies
