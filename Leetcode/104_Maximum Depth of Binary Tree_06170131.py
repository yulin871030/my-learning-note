# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None: return 0
        queue = [root]
        level = 0
        while len(queue) > 0:
            tmp = []
            level +=1
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            queue = tmp
        return level
