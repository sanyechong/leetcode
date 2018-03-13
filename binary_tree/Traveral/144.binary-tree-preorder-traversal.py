# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list_r = []
        list_m = []
        while True:
            if root:
                list_r.append(root.val)
                if root.left:
                    if root.right:
                        list_m.append(root.right)
                    root = root.left
                elif root.right:
                    root = root.right
                else:
                    if list_m:
                        root = list_m[-1]
                        list_m.remove(root)
                    else:
                        break
            else:
                break
        return list_r
        
        
        
