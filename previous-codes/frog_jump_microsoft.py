"""
Given an array of integers called "blocks" of size N, where each integer represents the size of a block, two frogs aim to maximize the distance 
between them. They start either on the first block or the "optimal starting block" and can jump only to adjacent blocks with equal or greater size.  
The distance between blocks J and K (J ≤ K) is computed as K - J + 1. The task is to determine the maximum distance the frogs can achieve when 
starting from the optimal block.
"""
def distance(i, j):
    if i <= j:
        return j-i+1
    else:
        return i-j+1

def solution(blocks):
    N = len(blocks)
    maxRangeRight = [0] * N
    maxRangeLeft = [0] * N
    for i in range(N-2,-1,-1):
        if blocks[i] <= blocks[i+1]:
            maxRangeRight[i] = maxRangeRight[i+1] + 1
        else:
            continue
    for j in range(1,N):
        if blocks[j] <= blocks[j-1]:
            maxRangeLeft[j] = maxRangeLeft[j-1] + 1
        else:
            continue
    sumjumps = []
    maxIndex = -1
    maxVal = 0
    for index in range(N):
        sumjumps.append(maxRangeLeft[index]+maxRangeRight[index])
        if maxRangeLeft[index]+maxRangeRight[index] >= maxVal:
            maxVal = maxRangeLeft[index]+maxRangeRight[index]
            maxIndex = index
    finalPos1 = max(0, maxIndex-maxRangeLeft[maxIndex])
    finalPos2 = min(N-1, maxIndex+maxRangeRight[maxIndex])
    print(maxRangeLeft, maxRangeRight, maxIndex, finalPos1, finalPos2)
    return distance(finalPos1, finalPos2)

inputs = [1,5,5,2,6]
print(solution(inputs))
        
    