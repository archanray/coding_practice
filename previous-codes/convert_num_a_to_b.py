# code to convert a number from a to b
# constraints:
# 1. divide by 7 when its a multiple of 7
# 2. divide by 3 if its a multiple of 3
# 3. subtract 1 
# 4. add 1
# if b is > a, you can only increase 1
from collections import deque
class Solution:
    def minimumOperationsToMakeEqual(self, a, b):
        # handle the case when b>=a and we can only increase by 1 to reach
        if b >= a:
            return b-a

        queue = deque()
        visited = set()
        queue.append(a)
        operations = 0
        
        while queue:
            n = len(queue)
            # evaluations in one level
            for _ in range(n):
                current = queue.popleft()
                if current == b:
                    return operations
                if current in visited:
                    continue
                visited.add(current)
                queue.append(current+1)
                if current > 1:
                    queue.append(current-1)
                if current % 11 == 0:
                    queue.append(current//11)
                if current % 5 == 0:
                    queue.append(current//5)
            operations+=1
                
        return -1

print(Solution().minimumOperationsToMakeEqual(26,1))
