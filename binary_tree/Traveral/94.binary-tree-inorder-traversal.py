class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list_m = []
        result = []
        while root or list_m:
            if root:
                list_m.append(root)
                root = root.left
            else:
                root = list_m.pop()
                result.append(root.val)
                root = root.right
        return result
