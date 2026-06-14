# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        path = []
        
        # def dfs(node):
        #     if not node:
        #         path.append("N")
        #         return
        #     path.append(str(node.val))
        #     dfs(node.left)
        #     dfs(node.right)
        #   dfs(root)
        if not root:
            return ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                path.append(str(node.val))
                print(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                path.append("N")
      
        return ",".join(path)            

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        root = TreeNode()
        vals = data.split(",")
        root.val = vals[0]
        if not data:
            return None            
        
        index = 1
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if index<len(data) and vals[index]!="N":
                node.left = TreeNode(int(vals[index]))
                queue.append(node.left)
            index+=1
            if index<len(data) and vals[index]!= "N":
                node.right = TreeNode(int(vals[index]))
                queue.append(node.right)
            index+=1

        return root





        return root