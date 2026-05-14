import string
class Solution:
    def isPalindromeOwn(self, s: str) -> bool:
        """
        solution:
        start witha pointer on the left and one on the right, 
        if they match keep increasing and decreasing respectively,
        else return False
        Space complexity O(1)
        Time complexity O(n)
        """
        left = 0
        right = len(s)-1
        num_list = list(map(str, list(range(10))))
        sets_valid = set(list(string.ascii_lowercase) + num_list)

        while left < right:
            if s[left].lower() not in sets_valid:
                left = left+1
                continue
            if s[right].lower() not in sets_valid:
                right = right-1
                continue
            if right < left:
                return True
            if s[left].lower() != s[right].lower():
                print(s[left], s[right], left, right)
                return False
            else:
                left = left+1
                right = right-1
        return True

    def isPalindrome(self, s: str) -> bool:
        """
        same as above but much faster
        """
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

q = Solution()
print(q.isPalindrome("Was it a car or a cat I saw?"))