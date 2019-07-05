class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def removeNthFromEnd(self, head, n):
		dummy = ListNode(0)
		dummy.next = head
		fast = slow = dummy
		for _ in range(n):
			fast = fast.next
		while fast and fast.next:
			fast = fast.next
			slow = slow.next
		slow.next = slow.next.next
		return dummy.next

if __name__ == "__main__":
	sol = Solution()
	head = ListNode(1)
	a = ListNode(2)
	b = ListNode(3)
	c = ListNode(4)
	d = ListNode(5)
	head.next = a
	a.next = b
	b.next = c
	c.next = d
	d.next = None
	res = sol.removeNthFromEnd(head, 2)
	while res:
		print(res.val)
		res = res.next