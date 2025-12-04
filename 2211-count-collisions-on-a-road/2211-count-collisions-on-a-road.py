class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        
        for c in directions:
            if c == 'R':
                stack.append('R')
            
            elif c == 'S':
                # All previous R must collide with this S
                while stack and stack[-1] == 'R':
                    collisions += 1
                    stack.pop()
                stack.append('S')
            
            else:  # c == 'L'
                if not stack:
                    stack.append('L')
                    continue
                
                if stack[-1] == 'R':
                    # First R-L collision: +2
                    collisions += 2
                    stack.pop()
                    
                    # Any remaining R's will collide with resulting S
                    while stack and stack[-1] == 'R':
                        collisions += 1
                        stack.pop()
                    
                    # Resulting car becomes 'S'
                    stack.append('S')
                
                elif stack[-1] == 'S':
                    # L hits S → +1
                    collisions += 1
                    stack.append('S')
                
                else:  # stack[-1] == 'L'
                    # No collision
                    stack.append('L')
        
        return collisions