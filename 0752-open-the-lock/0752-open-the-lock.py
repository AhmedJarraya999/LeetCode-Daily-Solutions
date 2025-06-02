class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit=set()
        dead=set(deadends)
        if "0000" in dead:
            return -1
        def children(lock):
            res=[]
            for i in range(4):
                digit=str((int(lock[i])+1)%10)
                res.append(lock[:i]+digit+lock[i+1:]) #since string are immutable
                digit=str((int(lock[i])-1+10)%10)  #to handle edge case negative value mod 10
                res.append(lock[:i]+digit+lock[i+1:])
            return res
        q=deque()
        q.append(["0000",0]) #lock value+ steps
        while q:
            lock,steps=q.popleft()
            if lock==target:
                return steps
            for child in children(lock):
                if child not in visit and child not in dead:
                    visit.add(child)
                    q.append([child,steps+1])
        return -1
                





        #TLE SOLUTION        
        # visit=set()
        # dead=set(deadends)

        # if "0000" in dead:
        #     return -1

        # min_steps=[float('inf')]
        # def backtrack(node,steps):
        #     if node in dead or node in visit:
        #         return
        #     if steps>min_steps[0]:
        #         return
        #     if node==target:
        #         min_steps[0]=steps
        #     visit.add(node)
        #     for i in range(4):
        #         digit =int(node[i])
        #         for move in [-1,1]:
        #             new_digit = (digit + move) % 10 #to avoid 10 wehen incrementing
        #             next_node = node[:i] + str(new_digit) + node[i+1:]
        #             backtrack(next_node, steps + 1)
        #     visit.remove(node)
        # backtrack("0000", 0)
        # return min_steps[0] if min_steps[0]!=float('inf') else -1
            


        