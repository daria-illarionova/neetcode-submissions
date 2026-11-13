# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index_of = {val: i for i, val in enumerate(inorder)}   # value -> position
        pre_idx = 0                                             # next root in preorder

        def build(lo: int, hi: int) -> TreeNode | None:         # subtree = inorder[lo..hi], inclusive
            nonlocal pre_idx
            if lo > hi:                                         # FIX 1: empty range (lo == hi is one node)
                return None
            root_val = preorder[pre_idx]
            pre_idx += 1
            root = TreeNode(root_val)
            mid = index_of[root_val]
            root.left = build(lo, mid - 1)                      # FIX 2: everything left of the root
            root.right = build(mid + 1, hi)                     # FIX 3: everything right of the root
            return root

        return build(0, len(inorder) - 1)
        