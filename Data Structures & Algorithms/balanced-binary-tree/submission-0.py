# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node: TreeNode | None) -> int:
            if node is None:
                return 0
            
            height_left = height(node.left)
            if height_left < 0:
                return -1
            height_right = height(node.right)
            if height_right < 0:
                return -1

            if abs(height_left - height_right) > 1:
                return -1
            return max(height_left, height_right) + 1
        
        return height(root) != -1
        