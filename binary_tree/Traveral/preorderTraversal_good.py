class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        list_r = []
        stack = [root]
        if not root:
            return list_r
        while stack:            
            root = stack.pop()
            list_r.append(root.val)
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)  
        return list_r
