class Solution:
    def isValid(self, s: str) -> bool:
        check_dict = {}
        check_dict[")"] = "("
        check_dict["}"] = "{"
        check_dict["]"] = "["

        n = len(s)
        if n % 2 != 0:
            return False
        if n == 0:
            return True
        stack_res = []
        for i in range(n):
            if s[i] not in check_dict.keys():
                stack_res.append(s[i])
            else:
                try:
                    if stack_res[-1] == check_dict[s[i]]:
                        stack_res.pop()
                    else:
                        stack_res.append(s[i])
                except:
                    return False
        if len(stack_res) > 0:
            return False
        else:
            return True

    def simpleIsValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False


q = Solution()
inputs = "]]"
print(q.isValid(inputs))