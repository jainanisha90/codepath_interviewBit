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
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        current = dummy = ListNode(-1)
        while A and B:
            if A.val < B.val:
                current.next = A
                A = A.next
            else:
                current.next = B 
                B = B.next
            current = current.next
        current.next = A or B
        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(5)
    l1.next = ListNode(8)
    l1.next.next = ListNode(20)
    l2 = ListNode (4)
    l2.next = ListNode(11)
    l2.next.next = ListNode(15)
    print Solution().mergeTwoLists(l1, l2) # Output 4 -> 5 -> 8 -> 11 -> 15 -> 20

