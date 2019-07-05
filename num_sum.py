def fourSum(nums, numbers, target):
    nums.sort()
    results = []
    findNsum(nums, target, numbers, [], results)
    return results

def findNsum(nums, target, N, result, results):
    if len(nums) < N or N < 2: return

    # solve 2-sum
    if N == 2:
        l,r = 0,len(nums)-1
        while l < r:
            if nums[l] + nums[r] == target:
                results.append(result + [nums[l], nums[r]])
                l += 1
                r -= 1
                while l < r and nums[l] == nums[l - 1]:
                    l += 1
                while r > l and nums[r] == nums[r + 1]:
                    r -= 1
            elif nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    else:
        for i in range(0, len(nums)-N+1):   # careful about range
            if target < nums[i]*N or target > nums[-1]*N:  # take advantages of sorted list
                break
            if i == 0 or i > 0 and nums[i-1] != nums[i]:  # recursively reduce N
                findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)
    return

nums = [215.09, 14563.11, 29126.21, 173.92, 55.07, 168.93, 64.53, 900.41, 160.19 ,550.49, 847.54, 129.44, 1618.52, 198.11, 4925.67, 358.88, 40.68, 98.8, 363.28, 85.56, 82.98, 110.26, 106.3, 3956.64, 915.38, 711.97, 276.07]

for i in range(1, 28):
    results = fourSum(nums, i, 50657.65)
    print(i, results)

n_list = [64.53, 160.19, 168.93, 198.11, 550.49, 900.41, 4925.67, 14563.11, 29126.21]
print(sum(n_list))


