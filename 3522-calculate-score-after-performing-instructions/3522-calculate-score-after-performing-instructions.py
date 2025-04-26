class Solution(object):
    def calculateScore(self, instructions, values):
        res = 0
        visited = set()
        pos = 0
        
        while 0 <= pos < len(instructions) and pos not in visited:
            visited.add(pos)
            if instructions[pos] == "add":
                res += values[pos]
                pos += 1
            elif instructions[pos] == "jump":
                pos += values[pos]
        
        return res
        