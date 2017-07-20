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
    # @return the head node in the linked list
    def insertionSortList(self, A):
        if A is None or self.isSorted(A):
            return A
        
        dummy = ListNode(-2147483648)
        dummy.next = A
        cur, sorted_tail = A.next, A
        while cur:
            prev = dummy
            while prev.next.val < cur.val:
                prev = prev.next
            if prev == sorted_tail:
                cur, sorted_tail = cur.next, cur  
            else:
                cur.next, prev.next, sorted_tail.next = prev.next, cur, cur.next
                cur = sorted_tail.next
                
        return dummy.next
    
    def isSorted(self, head):
        while head and head.next:
            if head.val > head.next.val:
                return False
            head = head.next
        return True

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(3)
    l1.next.next = ListNode(2)
    print Solution().insertionSortList(l1) # Output 1->2->3

