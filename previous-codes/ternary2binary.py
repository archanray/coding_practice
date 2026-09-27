# defining a node in a tree
class Node():
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# class for solving the ternary expression to binary tree
class Solution():
    def terExpToBinTree(self, expression, index):
        if index >= len(expression):
            return None

        root = Node(expression[index])
        index += 1

        if (index < len(expression)) and (expression[index] == "?"):
            root.left = self.terExpToBinTree(expression, index+1)
        if (index < len(expression)) and (expression[index] == ":"):
            root.right = self.terExpToBinTree(expression, index+1)

        return root

    def printTree(self, root):
        if not root:
            return
        print(root.data, end=" ")

        self.printTree(root.left)
        self.printTree(root.right)

string_expression = "a?b?c:d:e"
q = Solution()
root_node = q.terExpToBinTree(string_expression, 0)
q.printTree(root_node)