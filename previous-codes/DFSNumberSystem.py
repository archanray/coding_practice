class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def DFS(self, root, path):
        path += str(root.val)
        if root.right is None and root.left is None:
            self.allpath.append(path)
            return
        if root.left:
            self.DFS(root.left, path)
        if root.right:
            self.DFS(root.right, path)
        return
    
    def sumRootToLeaf(self, allPath):
        vals = [int(x) for x in allPath]
        return sum(vals)
    
    def sumNumbers(self, root):
        self.allpath = []
        self.DFS(root, "")
        return self.sumRootToLeaf(self.allpath)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

q = Solution()
print("sum of all root to leaf:", q.sumNumbers(root))