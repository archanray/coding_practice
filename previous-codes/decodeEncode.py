class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.left = left
        self.right = right
        self.val = val
        pass

class Solution:
    def buildTreeHelper(self, preorder, left, right):
        if left > right:
            return None
        rootval = preorder[self.preorderID]
        self.preorderID += 1
        root = TreeNode(rootval)
        pivotID = self.map_inorder[rootval]
        root.left = self.buildTreeHelper(preorder, left, pivotID-1)
        root.right = self.buildTreeHelper(preorder, pivotID+1, right)
        return root
    
    def buildTree(self, preorder, inorder):
        # expected all are unique elements
        if not preorder or not inorder:
            return None
        self.map_inorder = {val:idx for idx,val in enumerate(inorder)}
        self.preorderID = 0
        return self.buildTreeHelper(preorder, 0, len(preorder)-1)

    def encodeTreePreorder(self, rootNode):
        if not rootNode.left == None:
            self.encodeTreePreorder(rootNode.left)
        if not rootNode.right == None:
            self.encodeTreePreorder(rootNode.right)
        self.preorder.append(rootNode.val)
        return None
    
    def encodeTreeInorder(self, rootNode):
        if not rootNode.left == None:
            self.encodeTreeInorder(rootNode.left)
        self.inorder.append(rootNode.val)
        if not rootNode.right == None:
            self.encodeTreeInorder(rootNode.right)
        return None
    
    def encodeTree(self, rootNode):
        self.preorder = []
        self.inorder = []
        self.encodeTreePreorder(rootNode)
        self.encodeTreeInorder(rootNode)
        return self.preorder, self.inorder

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
q = Solution()
fullTreeRoot = q.buildTree(preorder, inorder)

print(q.encodeTree(fullTreeRoot))


##### For Leetcode format
# input is a level order traversal of a binary tree with nulls indicating missing nodes
# reusing tree structure as before
class Codec:
    def deserialize(self, traversal):
        # construct tree from level order traversal
        if len(traversal) == 0:
            return None
        split_vals = traversal.split(",")
        if split_vals[0] == "null":
            return None
        # remove the trailing null
        queue = []
        root = TreeNode(int(split_vals[0]))
        queue.append(root)
        idx = 0
        while len(queue) != 0:
            node = queue.pop(0)
            idx += 1
            if split_vals[idx] == "null":
                node.left = None
            else:
                node.left = TreeNode(int(split_vals[idx]))
                queue.append(node.left)
            idx += 1
            if split_vals[idx] == "null":
                node.right = None
            else:
                node.right = TreeNode(int(split_vals[idx]))
                queue.append(node.right)
        return root
            
    
    def serialize(self, root):
        # construct a level order traversal of the tree
        # root: TreeNode
        s = ""
        queue = []
        queue.append(root)
        while len(queue) != 0:
            node = queue.pop(0)
            if node == None:
                s += "null,"
                continue
            s += str(node.val) + ","
            if node != None:
                queue.append(node.left)
                queue.append(node.right)
        return s[:-1]

root = "1,2,3,null,null,4,5,null,null,null,null"
ser = Codec()
deser = Codec()
ans = deser.deserialize(ser.serialize(deser.deserialize(root)))
print(ans) # [1,2,3,null,null,4,5]