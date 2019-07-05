class Solution:
    def searchRange(self, nums, target: int):
        l, r = 0, len(nums)
        res = [-1, -1]
        while l < r:
            mid = (l + r) // 2
            if target == nums[mid]:
                start = end = mid
                while 0 <= start-1 and target == nums[start]:
                    start -= 1
                while end+1 <= r-1 and target == nums[end]:
                    end += 1
                res = [start+1, end-1]
                break
            elif target < nums[mid]:
                r = mid-1
            elif target > nums[mid]:
                l = mid+1
        return res

if __name__ == '__main__':
	nums = [1,3]
	target = 3
	sol = Solution()
	res = sol.searchRange(nums, target)
	print(res)