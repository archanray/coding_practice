class TreeNode:
    def __init__(self,val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def maxDepthHelper(self, node, depth):
        if node == None:
            return depth
        return max(self.maxDepthHelper(node.left, depth+1), self.maxDepthHelper(node.right, depth+1))

    def maxDepth(self, root):
        if root == None:
            return 0
        return self.maxDepthHelper(root, 0)