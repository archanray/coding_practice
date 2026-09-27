class Solution():
	def findGate(self, rooms):
		# grid is a list of lists
		# perform operations in place
		# dfs from each gate
		wall = -1
		gate = 0
		unknown = 2147483647

		if not rooms or not rooms[0]:
			return
		
		numRows = len(rooms)
		numCols = len(rooms[0])

		currLevel = []

		for i in range(numRows):
			for j in range(numCols):
				if rooms[i][j] == gate:
					currLevel.append( (i,j) )

		while currLevel:
			nextLevel = []
			for i, j in currLevel:
				currDist = rooms[i][j]

				for nextI, nextJ in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
					if 0<=nextI<numRows and 0<=nextJ<numCols and \
								rooms[nextI][nextJ] == unknown:
						rooms[nextI][nextJ] = currDist + 1
						nextLevel.append( (nextI,nextJ) )
			currLevel = nextLevel

		return rooms



Input= [[2147483647,  -1,  0,  2147483647],
		[2147483647, 2147483647, 2147483647,  -1],
		[2147483647,  -1, 2147483647,  -1],
		[0, -1, 2147483647, 2147483647]]
q = Solution()
print(q.findGate(Input))