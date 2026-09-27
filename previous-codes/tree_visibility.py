class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.visible = True

# basic idea is to do a BFS and then print traverse accordingly
class VisualizeTree:
    def BFS(self, node, level):
        # compute BFS of a tree and store the result in a list of lists
        if len(self.BFSList) == level:
            self.BFSList.append([node.val])
            self.VisibilityList.append([node.visible])
        else:
            self.BFSList[level].append(node.val)
            self.VisibilityList[level].append(node.visible)
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
    def traverseListofLists(self, BFSList, VisibilityList, side="right"):
        if side == "right":
            index = -1
        else:
            index = 0
        depth = len(BFSList)
        observableNodeVals = []
        for i in range(depth):
            if VisibilityList[i][index] == True:
                observableNodeVals.append(BFSList[i][index])
            else:
                if side == "left":
                    for j in range(index+1, len(BFSList[i])):
                        if VisibilityList[i][j] == True:
                            observableNodeVals.append(BFSList[i][j])
                            break
                if side == "right":
                    localRightIndex = len(BFSList[i])-1
                    for j in range(localRightIndex-1, -1, -1):
                        if VisibilityList[i][j] == True:
                            observableNodeVals.append(BFSList[i][j])
                            break
        return observableNodeVals
                
    def visibleNodes(self, root, side="right"):
        self.BFSList = []
        self.VisibilityList = []
        # compute BFS first
        self.BFS(root, 0)
        if side == None:
            observedNodes = self.BFSList
        else:
            observedNodes = self.traverseListofLists(self.BFSList, self.VisibilityList, side=side)
        return observedNodes

# Example usage:
# Constructing a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.left.visible = False
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.left.visible = False
root.right.right = TreeNode(7)
root.right.right.visible = False

q = VisualizeTree()
print("Full Tree:", q.visibleNodes(root, None))
print("Visible from left:", q.visibleNodes(root, "left"))
print("Visible from right:", q.visibleNodes(root, "right"))