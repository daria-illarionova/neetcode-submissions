# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_path = 0

        def height(node: TreeNode | None) -> int:
            nonlocal max_path
            if node is None:
                return 0
            left = height(node.left)
            right = height(node.right)
            max_path = max(max_path, left+right) # the path bending at this node
            return max(left, right) + 1  # this node's height, for its parent
        height(root)
        return max_path
        