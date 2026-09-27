class Solution:
    def dfs(self, course, visited):
        """
        cycle detection with topological sort
        """
        if visited[course] == 1:
            return False
        if visited[course] == -1:
            return True
        visited[course] = 1
        for prereq in self.adj[course]:
            if not self.dfs(prereq, visited):
                return False
        visited[course] = -1
        return True
    
    def canFinish(self, numCourses, prereqs):
        # create adj list of graph
        self.adj = [[] for _ in range(numCourses)]
        for course,prereq in prereqs:
            self.adj[course].append(prereq)
        # perform DFS
        visited = [0] * numCourses
        for course in range(numCourses):
            if not self.dfs(course, visited):
                return False
        return True

# numcourses = 2
# prereqs = [[1,0]]
# numcourses = 5
# prereqs = [[1,4],[2,4],[3,1],[3,2]]
# numCourses = 10
# prereqs = [[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]]
numCourses = 10
prereqs = [[5,8],[3,5],[1,9],[4,5],[0,2],[7,8],[4,9]]
q = Solution()
print(q.canFinish(numCourses, prereqs)) # True