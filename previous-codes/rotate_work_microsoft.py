from collections import deque
def nonOptimalSolution(T):
    """
    inefficient solution
    """
    if len(T) == 0:
        return 0
    if len(T) == 1:
        return T[0]
    queue = deque(T)
    total_time = 0
    time = 0
    while queue:
        current = queue.popleft()
        current -= 1
        if current > 0:
            queue.append(current)
        else:
            time += total_time + 1
        total_time += 1
    return time

def solution(jobs):
    mod = 1e9 + 7
    # Create pairs of (load, index)
    job_index_pair = [(job, i) for i, job in enumerate(jobs)]
    # Sort by load, then by index
    job_index_pair.sort(key=lambda x: (x[0], x[1]))
    
    timer = 0
    res = 0
    done = set()
    n = len(jobs)
    
    left, right = 0, 0
    # this runs until right == n, which can take at most O(n) steps
    while True:
        # increase right until the load requirement changes
        while right < n and job_index_pair[right][0] == job_index_pair[left][0]:
            right += 1
        timer += (n - left) * (job_index_pair[left][0] - (job_index_pair[left - 1][0] if left > 0 else 0) - 1)
        for i in range(left, right):
            res = (res + timer + job_index_pair[i][1] + 1 - len(done.intersection(set(range(job_index_pair[i][1] + 1))))) % mod
        timer += n - left
        if right == n:
            break
        for i in range(left, right):
            done.add(job_index_pair[i][1])
        left = right
    return int(res)

if __name__ == "__main__":
    input = [3,1,2]
    print(solution(input)) 
    input = [7,7,7]
    print(solution(input))
    input = [10000]
    print(solution(input))
    input = [1,2,3,4]
    print(solution(input))
    input = [1,2,3,4,5,6,7,8,9,10]
    print(solution(input))
    input = [1,1,1,1,1,1,1,1,1,1]
    print(solution(input))
    