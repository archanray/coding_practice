class Solution():
    def preprocessor(self, s):
        n = len(s)
        lookup = [0]*n
        j = 0
        i = j+1
        while i < n:
            if s[i] == s[j]:
                j = j+1
                lookup[i] = j
                i = i+1
            else:
                if j != 0:
                    j = lookup[j-1]
                else:
                    lookup[i] = 0
                    i = i+1
        return lookup

    def KMPsolver(self, s1, s2):
        s1 = s1+s1
        lookup = self.preprocessor(s2)
        i, j, n, m = 0, 0, len(s1), len(s2)

        while i < n and j < m:
            if s1[i] == s2[j]:
                i, j = i+1, j+1
                if j == m:
                    return True
            else:
                if j != 0:
                    j = lookup[j-1]
                else:
                    i = i+1
        return False
        
    def pythonSolver(self, s1, s2):
        s1 = s1+s1
        if s2 in s1:
            return True
        else:
            return False

    def dequeMethod(self, s1, s2):
        # first do an n check to see if the strings are lined up
        # bad and slow code!
        if s1 == s2:
            return True
        # make dequeues of s1 and s2
        q1, q2 = deque(s1), deque(s2)

        i = 0
        while i < len(s1):
            q1.append(q1.popleft())
            if q1 == q2:
                return True
            i += 1
        return False


    def rotateString(self, s, goal) -> bool:
        # base cases
        if len(s) != len(goal):
            return False
        if len(s) == 0:
            return True

        # return self.KMPsolver(s, goal)
        # return self.pythonSolver(s, goal)
        return self.dequeMethod(s, goal)

q = Solution()
s1 = "abcde"
s2 = "cdeab"
print(q.rotateString(s1, s2))

