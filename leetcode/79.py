class Solution:
	def exist(self, board, word):
		if not board:
			return False
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.dfs(board, i, j, word):
					return True
		return False

	# check whether can find word, start at (i,j) position
	def dfs(self, board, i, j, word):
		if len(word) == 0:  # all the characters are checked
			return True
		if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
			return False
		tmp = board[i][j]  # first character is found, check the remaining part
		board[i][j] = "#"  # avoid visit agian
		# check whether can find "word" along one direction
		res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) \
		      or self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
		board[i][j] = tmp
		return res

	def exist1(self, board, word: str) -> bool:
		if not board:
			return False
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.helper(board, i, j, word):
					return True
		return False

	def helper(self, board, i, j, word):
		if 0 == len(word):
			return True
		if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
			return False
		temp = board[i][j]
		board[i][j] = '#'
		res = self.helper(board, i - 1, j, word[1:]) or self.helper(board, i + 1, j, word[1:]) \
		      or self.helper(board, i, j - 1, word[1:]) or self.helper(board, i, j + 1, word[1:])

		board[i][j] = temp
		return res

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = 'ABCCED'
res = Solution().exist(board, word)
res1 = Solution().exist1(board, word)
print('res', res)
print('res1', res1)
