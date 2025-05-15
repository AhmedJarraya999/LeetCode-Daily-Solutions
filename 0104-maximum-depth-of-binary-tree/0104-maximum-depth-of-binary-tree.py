class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0
        level=0
        q = deque([root])
        while q:
            for i in range (len(q)):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level+=1
        return level


