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
    def removeNthFromEnd(self, A, B):
        
        current = A
        count = 0
        while current:
            current = current.next
            count += 1
        current = A
        element_index = count - B
        if element_index == 0 or element_index < 0:
            return A.next
        count = 0
        while current:
            count += 1
            if count == element_index:
                current.next = current.next.next
            current = current.next
        return A

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    print Solution().removeNthFromEnd(l1, 2) # Output 1->2->3->5

