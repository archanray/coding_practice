class Solution:
    def minimizedMaximum(self, n, quantities):
        # n specialty reality stores
        # quantities is the num of products of ith product type
        # distribute products as:
        # 1.  one store can get only one product type of indefinite quantity
        # 2. minimize maximum number of products given to any store
        low, high = 1, max(quantities)
        while low <= high:
            mid = low + (high-low) // 2
            totalRetails = 0
            for i in quantities:
                totalRetails += i // mid + (1 if i%mid != 0 else 0)
            if totalRetails > n:
                low = mid+1
            else:
                high = mid-1
        return low