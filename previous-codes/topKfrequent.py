import numpy as np
class Solution():
    def topKFrequent(self, nums, k):
        outputs = []
        n = len(nums)
        if n < k:
            return outputs

        # O(n log n)
        # nums = sorted(nums) # can avvoid this
        frequencies = {}
        # O(n), space O(n)
        for i in range(n):
            q = nums[i]
            if q not in frequencies.keys():
                frequencies[q] = 1
            else:
                frequencies[q] += 1

        vals = []
        keys = []
        # O(k), space: O(k)
        for ks in frequencies.keys():
            keys.append(ks)
            vals.append(frequencies[ks])

        # O(k log k)
        sortedIdxs = np.argsort(vals)

        vals = np.array(vals)[sortedIdxs.astype(int)]
        keys = np.array(keys)[sortedIdxs.astype(int)]

        # if len(keys) == 1 and k == 1:
        #     return keys

        if len(keys) < k:
            return list(keys)
        else:
            return list(keys[-1:-1-k:-1])

nums = [1]
k = 1
q = Solution()
print(q.topKFrequent(nums, k))