# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        mark_node = None
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                if not root.right or root.right is mark_node:
                    result.append(root.val)
                    mark_node = root
                    root = None
                else:
                    stack.append(root)
                    root = root.right
                    
        return result
