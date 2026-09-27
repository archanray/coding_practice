class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
# basic idea is to do a BFS and then print traverse accordingly
class Solution:
    def BFS(self, node, level):
        # compute BFS of a tree and store the result in a list of lists
        if len(self.BFSList) == level:
            self.BFSList.append([node.val])
        else:
            self.BFSList[level].append(node.val)
        if node.left == None and node.right == None:
            return
        elif node.right == None:
            self.BFS(node.left, level+1)
        elif node.left == None:
            self.BFS(node.right, level+1)
        else:
            self.BFS(node.left, level+1)
            self.BFS(node.right, level+1)
        return None
    
    def traverseZZ(self, BFSList):
        for i in range(len(BFSList)):
            if i % 2 != 0:
                BFSList[i] = BFSList[i][-1::-1]
        return BFSList        
                
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        self.BFSList = []
        # compute BFS first
        self.BFS(root, 0)
        observedNodes = self.traverseZZ(self.BFSList)
        return observedNodes

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(6)
# root.right.right = TreeNode(7)

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)

root = None

q = Solution()
print("Zigzag conversion:", q.zigzagLevelOrder(root))