# minimum possible value of max load time of servers if resources are allocated optimally
# LC: hard
class Solution:
    def minimumTimeRequired(self, jobs, k):
        if k == len(jobs):
            return max(jobs)
    
        self.min_val = float("inf")

        def backtrack(idx,ans):
            if idx == len(jobs):
                self.min_val = min(self.min_val,max(ans))
                return

            seen = set()

            for i in range(k):
                if ans[i] in seen: continue
                if ans[i] + jobs[idx] >= self.min_val: continue
                seen.add(ans[i])

                ans[i] += jobs[idx]
                backtrack(idx+1,ans)
                ans[i] -= jobs[idx]

        backtrack(0,[0]*k)

        return self.min_val

q = Solution()
print(q.minimumTimeRequired([1,2,4,7,8], 2)) # 7
