class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# Iterative solution.
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseBetween(self, head, m, n):
    	dummy = pre = ListNode(0)
    	dummy.next = head
	for _ in xrange(m-1):
        	pre = pre.next
        cur= pre.next
	# reverse the defined part 
        node = None
        for _ in xrange(n-m+1):
    	   	nxt = cur.next
	        cur.next = node
        	node = cur
	        cur= nxt
	# connect three parts
	pre.next.next = cur
	pre.next = node
	return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    print Solution().reverseBetween(head, 3, 4) # Output 1 -> 2 -> 4 -> 3 -> 5 -> None
