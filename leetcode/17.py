class Solution:
	def letterCombinations(self, digits):
		import functools
		if "" == digits:
			return []
		kvmaps = {
			'2': 'abc',
			'3': 'def',
			'4': 'ghi',
			'5': 'jkl',
			'6': 'mno',
			'7': 'pqrs',
			'8': 'tuv',
			'9': 'wxyz'
		}

		return functools.reduce(lambda xxx, digit: [x + y for x in xxx for y in kvmaps[digit]], digits, [''])
if __name__ == '__main__':
	sol = Solution()
	string = sol.letterCombinations("234")
	aa= lambda x, y: x+y
	print(aa(2,3))
	print(string)