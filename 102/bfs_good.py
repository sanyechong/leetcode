# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q_cur = [root]
        result_all = []

        while True:
            result = []
            for i in range(len(q_cur)):
                cur = q_cur.pop(0)
                result.append(cur.val)
                if cur.left:
                    q_cur.append(cur.left)
                if cur.right:
                    q_cur.append(cur.right)
            result_all.append(result)
            if len(q_cur) == 0:
                break
        return result_all

                
