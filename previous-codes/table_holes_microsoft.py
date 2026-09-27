import sys
def solution(nums):
    # O(n log n)
    nums = sorted(nums)
    n = len(nums)
    
    # max_size = sys.maxsize
    # # for left cover ending in index 0
    # max_size = min(1, nums[n-1]-nums[1])
    # # go from index 1 to n-2
    # for i in range(1,n-2):
    #     max_size = min(max_size, max(nums[i]-nums[0], nums[n-1]-nums[i+1]))
    # max_size = min(max_size, max(nums[n-2]-nums[0],1))
    
    preceq = [0] * n
    subseq = [0] * n
    
    preceq[0] = 1
    subseq[n-1] = 0
    subseq[n-2] = 1
    # O(n)
    for i in range(1,n):
        preceq[i] = nums[i] - nums[0]
    # O(n)
    for j in range(n-3,-1,-1):
        subseq[j] = nums[n-1] - nums[j+1]
    
    max_size = []
    # O(n)
    for i in range(n):
        max_size.append(max(preceq[i], subseq[i]))
    # O(n)
    return min(max_size)
    # return max_size

print(solution([15,20,9,11]))