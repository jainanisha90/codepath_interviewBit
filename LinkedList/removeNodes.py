# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self is None:
            return "Nil"
        else:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeElements(self, head, val):
        dummy = ListNode(float("-inf"))
        dummy.next = head
        prev, curr = dummy, dummy.next
        
        while curr:
            if curr.val > val:
                prev.next = curr.next
            else:
                prev = curr
            
            curr = curr.next
        
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(5)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(3)
    print Solution().removeElements(l1, 3) # Output 1->2->3->5

