class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        We want the longest window where we can make all characters the same using at most k replacements.
        The key insight is that the window is valid as long as:

        window size – count of the most frequent character ≤ k

        Why?
        Because the characters that aren't the most frequent are the ones we would need to replace.

        So while expanding the window, we track:

        the frequency of each character,
        the most frequent character inside the window (maxf).
        If the window becomes invalid, we shrink it from the left.
        This gives us one clean sliding window pass.
        """
        count = {}
        l = 0
        maxf = 0
        res = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) +1 
            maxf = max(maxf, count[s[r]])
            
            while (r-l+1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res