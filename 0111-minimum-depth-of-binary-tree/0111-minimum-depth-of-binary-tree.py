# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution: 
    def minDepth(self, root: TreeNode) -> int:

        if not root: return 0
        level, queue = 0, deque([root]) 

        while queue:

            level+= 1

            for x in range(len(queue)):

                n = queue.popleft()
                if not n.left and not n.right: return level

                if n.left : queue.append(n. left)
                if n.right: queue.append(n.right)
        