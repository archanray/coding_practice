# given a binary tree, each node has a value which represents 'water flow', separate the tree into 2 trees from the root, so that the difference between sum of water flows of each tree is minimal. this input is was 2 equal length arrays, first one described tree structure where arr[i] was the parent of this node, second one had each nodes value

# compute sum of subtree store in val
# total sum is stored in the root
# for any node, abs((totalSum - subtree sum) - subtreeSum) is the val we need to track!

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.postOrderSum = 0

class Solution:
    def totalSum(self, root):
        # compute using post order traversal
        if root == None:
            return 0
        root.postOrderSum = self.totalSum(root.left) + self.totalSum(root.right) + root.val
        return root.postOrderSum
    
    def findMinDiffSingle(self, root, val):
        if root == None:
            return
        leftDiff = abs(val+root.postOrderSum - 2*root.left.postOrderSum)
        rightDiff = abs(val+root.postOrderSum - 2*root.right.postOrderSum)
        
        self.minDiff = min(self.minDiff, leftDiff, rightDiff)
        return
    
    def findMinDiff(self, root):
        if root == None:
            return
        self.findMinDiffSingle(root, 0)
        self.findMinDiffSingle(root.left, root.right.postOrderSum+root.val)
        self.findMinDiffSingle(root.right, root.left.postOrderSum+root.val)
        return
    
    def minAbsDiff(self, root):
        import sys
        self.minDiff = sys.maxsize
        self.totalSum(root)
        self.findMinDiff(root)
        return self.minDiff

# Construct the tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

q = Solution()
print(q.minAbsDiff(root))