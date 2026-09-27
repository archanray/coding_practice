import math
class Solution():
	def dist(self, x1, x2):
		return math.sqrt((x2[0]-x1[0])**2 + (x2[1]-x1[1])**2)
		
	def bruteForce(self, xsorted):
		# compute brute fortce distance
		d1 = self.dist(xsorted[0], xsorted[1])
		d2 = self.dist(xsorted[0], xsorted[2])
		d3 = self.dist(xsorted[1], xsorted[2])
		if d1 <= d2 and d1 <= d3:
			return (xsorted[0], xsorted[1], d1)
		if d2 <= d1 and d2 <= d3:
			return (xsorted[0], xsorted[2], d2)
		if d3 <= d1 and d3 <= d2:
			return (xsorted[1], xsorted[2], d3)

	def rec(self, xsorted, ysorted):
		n = len(xsorted)
		if n == 3:
			q = self.bruteForce(xsorted)
			return q
		midpoint = xsorted[ n // 2 ]
		xsorted_left = xsorted[:n//2]
		xsorted_right = xsorted[n//2:]
		ysorted_left = []
		ysorted_right = []
		for point in ysorted:
			if point[0] <= midpoint[0]:
				ysorted_left.append(point)
			else:
				ysorted_right.append(point)
		(p1_left, p2_left, delta_left) = \
						self.rec(xsorted_left, ysorted_left)
		(p1_right, p2_right, delta_right) = \
						self.rec(xsorted_right, ysorted_right)
		if delta_left < delta_right:
			(p1, p2, delta) = (p1_left, p2_left, delta_left)
		else:
			(p1, p2, delta) = (p1_right, p2_right, delta_right)
		in_band = [point for point in ysorted if midpoint[0]-delta < \
					point[0] < midpoint[0]+delta]
		for i in range(len(in_band)):
			for j in range(i+1, min(i+7, len(in_band))):
				d = self.dist(in_band[i], in_band[j])
				if d < delta:
					(p1, p2, delta) = (in_band[i], in_band[j], d)
		return p1, p2, delta


	def findPairs(self, points):
		# first sort all points as per x axis and then y axis
		xsorted = sorted(points, key=lambda point:point[0])
		ysorted = sorted(points, key=lambda point:point[1])
		return self.rec(xsorted, ysorted)

nums = [[1,1],[3,3],[4,4],[5,5],[2,2]]
q = Solution()
print(q.findPairs(nums))