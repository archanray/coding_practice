class Solution():
    def findMedianSortedArrays(self, list1, list2)->float:
        # m+n is easy
        # count the length of the lists
        # then in a different list keep adding until m+n/2
        # we need a log (m+n) algorithm

        # ensure that list1 is smaller than list2
        if len(list1) > len(list2):
            list1, list2 = list2, list1

        # compute length of each lists (assuming this doesn't take m+n time)
        m, n = len(list1), len(list2)

        # set pointers for list1
        left, right = 0, m

        while left <= right:
            # partition the two lists
            mid1 = (left+right) // 2
            mid2 = (m+n+1) // 2 - mid1

            # find the maximum elements on the left of the partition
            max_l1 = list1[mid1-1] if mid1 > 0 else float("-inf")
            max_l2 = list2[mid2-1] if mid2 > 0 else float("-inf")
            max_left = max(max_l1, max_l2)

            # find the maximum elements on the right of the partition
            min_r1 = list1[mid1] if mid1 < m else float("inf")
            min_r2 = list2[mid2] if mid2 < n else float("inf")
            min_right = min(min_r1, min_r2)

            # check if partition is correct
            if max_left <= min_right:
                if (m+n)%2 == 0:
                    # condition when len is even
                    return (max_left+min_right) / 2
                else:
                    # condition when len is odd
                    return max_left
            elif max_l1 > min_r2:
                right = mid1 - 1
            else:
                left = mid1 + 1

q = Solution()
print(q.findMedianSortedArrays([1,3], [2]))