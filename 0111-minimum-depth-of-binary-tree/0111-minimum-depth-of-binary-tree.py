class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0
        stack=[(root,1)]
        minDepth=float('inf')
        while stack:
            node,depth=stack.pop()
            if not node.left and not node.right:
                minDepth = min(minDepth, depth)
            if node.left:
                stack.append((node.left,depth+1))
            if node.right:
                stack.append((node.right,depth+1))
        return minDepth

        