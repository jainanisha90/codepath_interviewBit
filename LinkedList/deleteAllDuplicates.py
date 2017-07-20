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
    def deleteAllDuplicates(self, A):
        current = A
        while current:
            next_node = current.next
            while next_node and current.val == next_node.val:
                next_node = next_node.next
            current.next = next_node
            current = next_node
        return A


head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
# 1->1->2
print Solution().deleteAllDuplicates(head) # Output 1->2
