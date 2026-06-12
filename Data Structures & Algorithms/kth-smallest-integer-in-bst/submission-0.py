# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #請幫我找出這棵樹裡面，
        # 第 k 小的數字是多少？（k=1 代表最小的，k=2 代表第二小的，以此類推）。
        path = []

        def DFS(node):

            if not node:
                return 
            DFS(node.left)
            path.append(node.val)
            DFS(node.right)

        DFS(root)
        return(path[k-1])