class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if self:
            return "{} ".format(self.val)
        
class Solution:
    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, A):
        fast, slow = A, A
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if fast is slow:
                fast = A
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = head.next
    print Solution().detectCycle(head)	#Output 2
