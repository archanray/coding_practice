class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        pass
class Solution:
    def dfs(self, node, current):
        n = len(current) 
        if n >= 4:
            return
        if n == 3:
            self.res.append(current)
        if node == None:
            return
        self.dfs(node.left, current+[node.val])
        self.dfs(node.right, current+[node.val])
        pass
            
    def solution(self, root):
        self.res = []
        self.dfs(root, [])
        returnVals = set()
        for i in range(len(self.res)):
            returnVals.add(self.res[i][0]*100 + self.res[i][1]*10 + self.res[i][2])
        return list(returnVals)

input = TreeNode(1)
input.left = TreeNode(2)
input.right = TreeNode(3)
input.left.left = TreeNode(4)
input.right.left = TreeNode(5)
input.right.right = TreeNode(6)

print(Solution().solution(input))