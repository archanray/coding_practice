# You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.
from collections import defaultdict, Counter, deque
class Solution:
    def alienOrder(self, words):
        # create an empty dict of list
        graph = defaultdict(list)
        # create a counter of the characters in the words
        # the counter is a dictionary with the characters as keys and the number of times they appear in the words as values
        # the characters are the keys of the dictionary
        # the values are the number of times the characters appear in the words
        # initially all characters get 0s
        indegree = Counter({c: 0 for word in words for c in word})
        # run FOR for all elements
        for i in range(len(words) - 1):
            # grab two words and check their parallel characters
            for a, b in zip(words[i], words[i + 1]):
                # if not same chars
                if a != b:
                    # add a directed edge to the graph
                    graph[a].append(b)
                    # increase indegree counter
                    indegree[b] += 1
                    # stop if the characters don't match
                    break
        # construct a doubly open queue
        # what does indegree[c] == 0 mean?
        # it means that the character c has no incoming edges
        # it means that the character c is the first character in the order
        queue = deque([c for c in indegree if indegree[c] == 0])
        # init empty string
        res = ''
        # run while the queue is not empty
        while queue:
            # pop the leftmost element from the queue
            c = queue.popleft()
            # add the character to the result
            res += c
            # run for all neighbors of the character
            for neighbor in graph[c]:
                # decrease the indegree of the neighbor
                indegree[neighbor] -= 1
                # if the indegree of the neighbor is 0, add it to the queue
                if indegree[neighbor] == 0:
                    # add the neighbor to the queue
                    queue.append(neighbor)
        # if the length of the result is not equal to the length of the indegree, return an empty string
        return res if len(res) == len(indegree) else ''
# Time complexity: O(C)
# Space complexity: O(C)
# Test cases:
# words = ["wrt","wrf","er","ett","rftt"]
# words = ["z","x","z"]
# words = ["z","x"]
words = ["z","x","z"]
q = Solution()
print(q.alienOrder(words)) # ""