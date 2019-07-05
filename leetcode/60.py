class Solution:
	def getPermutation(self, n: int, k: int) -> str:
		if 1 == n:
			return '1'
		temp = [i for i in range(1, n + 1)]
		count = 1
		res = ''
		while k:
			base = self.fact(n - count)
			pre = k // base
			if pre == k / base:
				res += str(temp.pop(pre-1))
				break
			else:
				k = k % base
				count += 1
				res += str(temp.pop(pre))

		res += ''.join(map(str, temp[::-1]))
		return res

	def fact(self, n):
		if 1 == n:
			return 1
		return n * self.fact(n - 1)


print(Solution().getPermutation(4, 9))