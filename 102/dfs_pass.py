# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = []

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        self.doLevel(root, 0)
        return self.result

    def doLevel(self, node: TreeNode, level):
        if len(self.result) == level:
            self.result.append([])
        self.result[level].append(node.val)
        if node.left:
            self.doLevel(node.left, level+1)
        if node.right:
            self.doLevel(node.right, level+1)
