class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def level(self, count, rootNode):
        if rootNode == None:
            return
        if len(self.result) <= count:
            self.result.append([])
        self.result[count].append(rootNode.val)
        count += 1
        self.level(count, rootNode.left)
        self.level(count, rootNode.right)
        
    def levelOrder(self, root):
        if root == None:
            return None
        self.result = []
        self.level(0, root)
        return self.result