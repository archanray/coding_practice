class Solution:
    def hIndex(self, citations: list[int]) -> int:
        """
        compute h-index for a given list of citations
        """
        if len(citations) == 0:
            return 0
        if len(citations) == 1:
            return min(1,citations[0])

        sortedCitations = sorted(citations)
        n = len(citations)
        hIdx = 0
        for i in range(n-1, -1, -1):
            if sortedCitations[i] > hIdx:
                hIdx += 1
            # print(sortedCitations[i], hIdx)
        return hIdx

q = Solution()
print(q.hIndex([3,0,6,1,5]))
print(q.hIndex([1,3,1,5]))

