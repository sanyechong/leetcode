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
        q_cur = []
        result_all = []

        q_cur.append(root)
        while True:
            result = []
            q_sub = []
            for i in q_cur:
                result.append(i.val)
                if i.left:
                    q_sub.append(i.left)
                if i.right:
                    q_sub.append(i.right)
            result_all.append(result)
            del q_cur
            q_cur = q_sub
            if len(q_sub) == 0:
                break
        return result_all

