class Solution:
	def threeSum(self, nums):
		res = []
		for i in range(len(nums) - 2):
			for j in range(i + 1, len(nums) - 1):
				for k in range(j + 1, len(nums)):
					if nums[i] + nums[j] + nums[k] == 0:
						a = nums[i] if min(nums[j], nums[k]) > nums[i] else min(nums[j], nums[k])
						b = nums[i] if max(nums[j], nums[k]) < nums[i] else max(nums[j], nums[k])
						c = -(a + b)
						if [a, c, b] not in res:
							res.append([a, c, b])

		return res

	def threeSum2(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length-2):
			if nums[i] > 0:
				break
			if i > 0 and nums[i] == nums[i-1]:
				continue

			l, r = i + 1, length - 1
			while l < r:
				total = nums[i] + nums[l] + nums[r]
				if total < 0:
					l += 1
				elif total > 0:
					r -= 1
				else:
					res.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l + 1]:
						l += 1
					while l < r and nums[r] == nums[r - 1]:
						r -= 1

					l += 1
					r -= 1
		return res


	def threeSum3(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length - 2):
			if nums[i] > 0:
				break
			if nums[i] == nums[i + 1]:
				continue

			l, r = i + 1, length - 1
			while l < r:
				total = nums[i] + nums[l] + nums[r]
				if total < 0:
					l += 1
				elif total > 0:
					r -= 1
				else:
					res.append([nums[i], nums[l], nums[r]])
					while l < r and nums[l] == nums[l + 1]:
						l += 1
					while l < r and nums[r] == nums[r - 1]:
						r -= 1

					l += 1
					r -= 1
		return res

if __name__ == '__main__':
	sol = Solution()
	#string = sol.threeSum([2,5,5,8,-7,-9,5,-1,-4,2,8,4,-6,-2,-2,9,-2,13,1,0,9,9,4,-13,13,3,-14,11,-5,-13,3,4,7,-15,-11,7,13,1,13,-14,11,-1,5,-10,12,11,14,-13,1,-8,3,-4,-14,14,-10,-15,-6,-9,3,-4,-7,-8,-15,8,-8,12,-8,13,-2,-9,14,-6,5,-3,-9,-6,-7,-10,-3,9,-2,7,-10,-9,-2,-5,13,7,-6,2,-12,-6,1,10,9,0,7,-13,-2,-9,-7,-2,-8,5,10,-1,6,-12,4,10,12,9,2,10,8,-15,12,6,-1,-9,-7,2])
	#string2 = sol.threeSum2([2,5,5,8,-7,-9,5,-1,-4,2,8,4,-6,-2,-2,9,-2,13,1,0,9,9,4,-13,13,3,-14,11,-5,-13,3,4,7,-15,-11,7,13,1,13,-14,11,-1,5,-10,12,11,14,-13,1,-8,3,-4,-14,14,-10,-15,-6,-9,3,-4,-7,-8,-15,8,-8,12,-8,13,-2,-9,14,-6,5,-3,-9,-6,-7,-10,-3,9,-2,7,-10,-9,-2,-5,13,7,-6,2,-12,-6,1,10,9,0,7,-13,-2,-9,-7,-2,-8,5,10,-1,6,-12,4,10,12,9,2,10,8,-15,12,6,-1,-9,-7,2])
	#print(string)
	string2 = sol.threeSum3([-1,0,1,2,-1,-4])
	print(string2)