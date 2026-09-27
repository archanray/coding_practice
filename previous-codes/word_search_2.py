# Given an m x n board of characters and a list of strings words, return all words on the board.

class Solution:
    def findWords(self, board, words):
        trie = {}
        for word in words:
            node = trie
            for w in word:
                if w not in node:
                    node[w] = {}
                node = node[w]
            node['#'] = word
        self.res = set()
        self.used = [[0] * len(board[0]) for _ in range(len(board))]
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in trie:
                    self.used[i][j] = 1
                    self.dfs(board, i, j, trie[board[i][j]], board[i][j])
                    self.used[i][j] = 0
        return list(self.res)
    def dfs(self, board, i, j, node, word):
        if '#' in node:
            self.res.add(node['#'])
        for dx, dy in self.dirs:
            x, y = i + dx, j + dy
            if 0 <= x < len(board) and 0 <= y < len(board[0]) and not self.used[x][y] and board[x][y] in node:
                self.used[x][y] = 1
                self.dfs(board, x, y, node[board[x][y]], word + board[x][y])
                self.used[x][y] = 0
#Time complexity: O(m*n*4^l) where m is the number of rows, n is the number of columns, and l is the length of the longest word in the list.
#Space complexity: O(m*n) for the used array and O(26^l) for the trie.
#Input
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
q = Solution()
print(q.findWords(board, words)) #Output: ["eat","oath"]