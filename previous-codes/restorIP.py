class Solution():
    def dfs(self, idx, path):
        if idx > len(self.s) or len(path) > 4:
            return
        if idx == len(self.s) and len(path) == 4:
            self.out.append(".".join(path))

        for i in range(1,4):
            if idx+i <= len(self.s) and int(self.s[idx:idx+i]) <= 255:
                if not (self.s[idx]=="0" and i>1):
                    self.dfs(idx+i, path+[self.s[idx:idx+i]])

    def restoreIpAddresses(self, s: str) -> list[str]:
        self.s = s
        self.out = []
        if not all(ord("0")<=ord(c)<=ord("9") for c in self.s):
            return self.out
        self.dfs(0, [])
        return self.out

q = Solution()
print(q.restoreIpAddresses("25525511135"))