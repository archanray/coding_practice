class Solution:
    def binSearchIndex(self, left):
        right = self.n
        while left < right:
            mid = left+((right-left) // 2)
            if self.arr[mid] == self.x:
                return mid
            elif self.arr[mid] > self.x:
                right = mid-1
            else:
                left = mid+1
        
        if left == self.n:
            return left-1
        if left == -1:
            return 0
        if self.arr[left] < self.x:
            return left
        else:
            return left-1
    
    def directionalSearch(self, idx):
        """
        runs in 2k time to return nearest k points
        """
        if idx == self.n-1:
            return self.arr[self.n-self.k:self.n]
        neighbors = []
        count = 0
        left = idx
        right = idx+1
        # print(count, self.k)
        while count < self.k:
            left_bal = abs(self.arr[left] - self.x)
            right_bal = abs(self.arr[right] - self.x)
            if right_bal < left_bal:
                neighbors.append(self.arr[right])
                count += 1
                right += 1
                if right == self.n:
                    break
            else:
                neighbors.insert(0, self.arr[left])
                count += 1
                left -= 1
                if left == -1:
                    break
            # print(neighbors, count)
                
        if count < self.k:
            balance = self.k-count
            # print("here", right, left, count)
            if right == self.n:
                left_adder = self.arr[left-balance+1:left+1]
                neighbors = left_adder + neighbors
            else:
                right_adder = self.arr[right:right+balance]
                neighbors = neighbors + right_adder
                
        return neighbors
        
    def findClosestElements(self, arr, k, x):
        """
        leetcode - 658
        arr: sorted array
        k: number of closest elements to return
        x: query
        """
        self.arr = arr
        self.x = x
        self.n = len(self.arr)
        self.k = k
        if self.n == 0 or self.n < k:
            return None
        immediateNeighborID = self.binSearchIndex(0)
        # print(self.arr[immediateNeighborID])
        vals = self.directionalSearch(immediateNeighborID)
        return vals
    
inputs = [1,5,10]
neighbors = 1
query = 4
q = Solution()
print(q.findClosestElements(inputs, neighbors, query))