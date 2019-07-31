class Solution:
	def maxProfit(self, prices):
		if not prices:
			return 0

		# forward traversal, profits record the max profit
		# by the ith day, this is the first transaction
		profits = []
		max_profit = 0
		current_min = prices[0]
		for price in prices:
			current_min = min(current_min, price)
			max_profit = max(max_profit, price - current_min)
			profits.append(max_profit)

		print(profits)

		# backward traversal, max_profit records the max profit
		# after the ith day, this is the second transaction
		total_max = 0
		max_profit = 0
		current_max = prices[-1]
		for i in range(len(prices) - 1, -1, -1):
			print(i)
			current_max = max(current_max, prices[i])
			max_profit = max(max_profit, current_max - prices[i])
			total_max = max(total_max, max_profit + profits[i])
		#print(max_profit)
		return total_max


prices = [1,2,4,2,5,7,2,4,9,8]
res = Solution().maxProfit(prices)
print(res)