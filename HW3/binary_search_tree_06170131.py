class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if val <= root.val:
            if root.left is None:
                root.left = TreeNode(val)
                return root.left
            else:
                return self.insert(root.left, val)
        else:
            if root.right is None:
                root.right = TreeNode(val)
                return root.right
            else:
                return self.insert(root.right, val)

    def maxValueNode(self, node):
        while node.right is not None:
            node = node.right
        return node

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        while self.search(root, target) is not None:
            if target > root.val:
                root.right = self.delete(root.right, target)
            elif target < root.val:
                root.left = self.delete(root.left, target)
            elif root.val == target:
                if root.left is None and root.right is None:
                    root = None
                    return None
                elif root.left is not None and root.right is None:
                    newnode = root.left
                    root = None
                    return newnode
                elif root.left is None and root.right is not None:
                    newnode = root.right
                    root = None
                    return newnode
                newnode = self.maxRightNode(root.left)
                root.val = newnode.val
                root.left = self.delete(root.left, newnode.val)
        return root





    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root is None:
            return
        else:
            if root.val == target:
                return root
            elif root.val > target:
                return self.search(root.left, target)
            elif root.val < target:
                return self.search(root.right, target)
            else:
                return None

    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        pass
    

