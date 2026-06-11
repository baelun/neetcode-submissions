# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        path = []
        def dfs(node):
            if not node:
                return 
            dfs(node.left)
            path.append(node.val)
            dfs(node.right)

        dfs(root)
        sort_path = sorted(path)
        if sort_path != path or len(set(path)) != len(path):
            return False
        else:
            return True