# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Version 1 inverted() + sameTree()
    '''
    def isSameTree(self, t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if t1 is None and t2 is None:                       # both None
            return True
        if t1 is None or t2 is None:                        # exactly one None
            return False
        return (t1.val == t2.val                            # values match
                and self.isSameTree(t1.left, t2.left)       # left with left
                and self.isSameTree(t1.right, t2.right))    # right with right
    
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        mirrored_left = self.invertTree(root.left)   # your 226 solution
        return self.isSameTree(mirrored_left, root.right)
    '''
    # Version 2 direct approach
    def isMirror(self, t1: TreeNode | None, t2: TreeNode | None) -> bool:
        if t1 is None and t2 is None:                       # both None
            return True
        if t1 is None or t2 is None:                        # exactly one None
            return False
        return (t1.val == t2.val                            # values match
                and self.isMirror(t1.left, t2.right)      # outside pair
                and self.isMirror(t1.right, t2.left))     # inside pair

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.isMirror(root.left, root.right) 
        