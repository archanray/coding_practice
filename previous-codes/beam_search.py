import numpy as np
from math import log

class Solution():
    def greedyDecoder(self, nums):
        # greedy decoder
        # index for largest probability in each row
        return [np.argmax(s) for s in nums]

    def beamSearch(self, nums, k):
        # algorithm for beam search
        sequences = [[list(), 0.0]]
        # walk over each step in a sequence
        for row in data:
            all_candidates = list()
            # expand each current candidate
            for i in range(len(sequences)):
                seq, score = sequences[i]
                for j in range(len(row)):
                    candidate = [seq+[j], score-log(row[j])]
                    all_candidates.append(candidate)
            # order candidates by their score
            ordered = sorted(all_candidates, key=lambda tup:tup[1])
            # select k best
            sequences = ordered[:k]
        return sequences

q = Solution()
# sequence of 10 words in a vocab of 5 words
data = [[0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1],
 [0.1, 0.2, 0.3, 0.4, 0.5],
 [0.5, 0.4, 0.3, 0.2, 0.1]]
data = np.array(data)
print(q.beamSearch(data, 3))