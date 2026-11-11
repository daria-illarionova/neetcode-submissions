# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def preorder(node: TreeNode | None):
            if node is None:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result

    ''' Version 2: Every recursive call builds a brand new list. So each value gets copied once for every ancestor above it.
    For a balances tree, O(n log n)
    RISK: On a skewed tree would have 1+ 2+ .. +n copies => O(n^2) time. 
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    '''
        