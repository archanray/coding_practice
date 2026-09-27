# given no. of shares available to distribute, and matrix of bidders, their bid price, and count of shares they want to buy, distribute the available shares from highest to lowest bidder. 
# there was 1 rule when multiple bidders have same price, round robin distribute until none left to distribute. find the bidder who didn't get any shares in the end.
import numpy as np

class Solution:
    def distrbuter(self, num_shares, bidding_matrix):
        # bidding_matrix: Nx2,, col1 -- bid price col2 -- count
        
        # sort column 1, and assign column 2 accordingly
        indices = np.argsort(bidding_matrix[:, 0].squeeze())
        indices = indices[::-1]
        bidding_matrix = bidding_matrix[indices,:]
        print(bidding_matrix)
        print(sum(bidding_matrix[:,1]))
        
        # then distribute in round robin if clashing
        n = len(bidding_matrix)
        assignment_matrix = []
        for i in range(n):
            request = bidding_matrix[i, 1]
            # print(bidding_matrix[i,0], request)
            if num_shares - request >= 0:
                assignment_matrix.append(request)
            else:
                assignment_matrix.append(num_shares)
            num_shares = num_shares - request
            if num_shares <= 0:
                break
        
        m = len(assignment_matrix)
        # in case of an ID column change this to read those columns only
        return assignment_matrix, indices[m:]
                

q = Solution()
total_shares = 300
input_matrix = np.array([[10, 40], [12, 50], [300, 10], [10, 100], [12, 30], [15, 140], [9, 120], [21, 21], [15, 120]])
print(q.distrbuter(total_shares, input_matrix))