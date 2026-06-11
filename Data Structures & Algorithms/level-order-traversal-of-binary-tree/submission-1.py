# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # if not root:
        #     return []     
        # result = []
        # queue = [root]

        # while queue:
        #     result.append([node.val for node in queue])
        #     queue = [child for node in queue for child in (node.left,node.right) if child]
        # return result

        # DFS
        result = [] #長度是0

        def order(node,index):
            if not node:
                return
            if len(result) == index: #從第一個node走是第0層
                result.append([])
          
            result[index].append(node.val)
            order(node.left,index+1)
            order(node.right,index+1)
        
        order(root,0)
        return result
        