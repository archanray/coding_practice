class Solution(object):
    def convertIndices(self, index):
        index_real = index+1
        if index_real % self.n == 0:
            row_id = index_real // self.n - 1
        else:
            row_id = index_real // self.n
        
        if index_real % self.n == 0:
            col_id = self.n - 1
        else:
            col_id = index_real % self.n - 1
        return row_id , col_id
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.m = len(matrix)
        self.n = len(matrix[0])
        total_elements = self.m * self.n

        # just do binary search on total elements
        start = 0
        end = total_elements-1
        while start <= end:
            mid = start+(end-start) // 2
            row_id, col_id = self.convertIndices(mid)
            if matrix[row_id][col_id] == target:
                return True

            if matrix[row_id][col_id] < target:
                start = mid+1
            if matrix[row_id][col_id] > target:
                end = mid-1
            print(mid)
        return False

q = Solution()
print(q.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 1))

        