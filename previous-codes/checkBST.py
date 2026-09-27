class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inOrderChk(self, root, prev):
        if root is not None:
            if not self.inOrderChk(root.left, prev):
                return False
            if prev[0] is not None and root.val <= prev[0].val:
                return False
            
            prev[0] = root
            return self.inOrderChk(root.right, prev)
        return True
    
    def isValidBST(self, root):
        prev = [None]
        return self.inOrderChk(root, prev)