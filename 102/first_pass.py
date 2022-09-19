# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result_all = []
        cur_layer = []
        cur_layer.append(root)
        while True:
            result = []
            next_layer = []
            for i in cur_layer:
                result.append(i.val)
                if i.left:
                    next_layer.append(i.left)
                if i.right:
                    next_layer.append(i.right)
            result_all.append(result)
            del cur_layer
            cur_layer = next_layer
            if not next_layer:
                break
        return result_all
