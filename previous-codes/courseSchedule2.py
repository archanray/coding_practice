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
        self.results.append(course)
        return True
    
    def findOrder(self, numCourses, prereqs):
        # create adj matrix of the courses
        self.adj = [[] for _ in range(numCourses)]
        for course, prereq in prereqs:
            self.adj[course].append(prereq)
        self.results = []
        
        # perform DFS
        visited = [0] * numCourses
        for course in range(numCourses):
            if visited[course] == 0 and not self.dfs(course, visited):
                return []
        return self.results
    
numCourses = 2
prerequisites = [[1,0]]
q = Solution()
print(q.findOrder(numCourses, prerequisites))