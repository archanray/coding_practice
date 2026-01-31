from collections import defaultdict
import heapq

class Solution():
    def hashTopKFrequent(self, nums: list, k: int) -> list[int]:
        """
        uses hashtable
        """
        hashtable = defaultdict(int)
        for n in nums:
            hashtable[n] = 1+hashtable.get(n, 0)
        pair_list = []
        for key in hashtable.keys():
            pair_list.append([hashtable[key], key])
        pair_list = sorted(pair_list, key=lambda x: x[0])
        vals = []
        for id in range(k):
            # print(id, vals)
            if id < k:
                # print(id, k)
                vals.append(pair_list[-1-id][1])
        return vals
    def topKFrequent(self, nums: list, k: int) -> list[int]:
        """
        uses min heap
        """
        hashtable = defaultdict(int)
        for n in nums:
            hashtable[n] = 1+hashtable.get(n, 0)
        min_heap = []
        for key in hashtable.keys():
            heapq.heappush(min_heap, (hashtable[key], key))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        vals = []
        for i in range(k):
            vals.append(heapq.heappop(min_heap)[1])
        return vals

q = Solution()
print(q.topKFrequent(nums = [7,7], k= 1))