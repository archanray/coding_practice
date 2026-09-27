class Solution:
    def hasPath(self, root, direction, x):
        if not root:
            return False
        if root.val == x:
            return True

        if self.hasPath(root.left, direction, x):
            direction.append("L")
            return True

        if self.hasPath(root.right, direction, x):
            direction.append("R")
            return True
    
        return False
    
    def getDirections(self, root, startValue, destValue):
        directionToStartValue = []
        directionToDestValue = []
        # find path from root to start node and dest node
        self.hasPath(root, directionToStartValue, startValue)
        self.hasPath(root, directionToDestValue, destValue)

        # reverse
        directionToStartValue = directionToStartValue[::-1]
        directionToDestValue = directionToDestValue[::-1]

        rs = ""
        i = 0

        # Find the index where the path starts in a different direction.
        while i < len(directionToStartValue):
            if i >= len(directionToDestValue) or directionToStartValue[i] != directionToDestValue[i]:
                break
            i += 1

        # add path from i to start value to result
        for j in range(i, len(directionToStartValue)): 
            rs += "U"

        # add path from i to dest value to result
        for j in range(i, len(directionToDestValue)): 
            rs += directionToDestValue[j]

        return rs