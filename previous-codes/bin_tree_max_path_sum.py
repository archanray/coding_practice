# Given the root of a binary tree, return the maximum path sum of any non-empty path.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        left = max(0, self.dfs(node.left))
        right = max(0, self.dfs(node.right))
        self.max_sum = max(self.max_sum, (left+right)+node.val)
        return max(left, right) + node.val
        
    def maxPathSum(self, root):
        self.max_sum = float("-inf")
        self.dfs(root)
        return self.max_sum

# test cases
# input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# output: 11
# input = TreeNode(1, TreeNode(2), TreeNode(3))
# output: 6
# input = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# output: 42
input = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
q = Solution()
print(q.maxPathSum(input)) # output: 6