class TreeNode():
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def minDepth(root):
	# condition to check if tree is empty
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return 1
	if root.left is None:
		return minDepth(root.right)+1
	if root.right is None:
		return minDepth(root.left)+1

	return min(minDepth(root.left), minDepth(root.right))+1

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print (minDepth(root))