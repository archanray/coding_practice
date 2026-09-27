class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = None
        pass

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

class Solution:
    def solution(self, root, leaf):
        current = leaf
        p = current.parent
        while current != root:
            gP = p.parent
            if current.left:
                current.right = current.left
            current.left = p
            p.parent = current
            if p.left == current:
                p.left = None
            if p.right == current:
                p.right = None
            current = p
            p = gP
        leaf.parent = None
        return leaf

input = "1,2,3,null,null,4,5,null,null,null,null"
# print(Codec().serialize(Codec().deserialize(input)))
Tree = Codec().deserialize(input)
print(Tree)
node = 5
print(Solution().solution(input, node))