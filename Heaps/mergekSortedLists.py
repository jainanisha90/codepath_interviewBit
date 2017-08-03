class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)

def mergeKLists(lists):
    
    def merge(lst1, lst2):
        dummy = pt = ListNode(-1)
        while lst1 and lst2:
            if lst1.val < lst2.val:
                pt.next = lst1
                lst1 = lst1.next
            else:
                pt.next = lst2
                lst2 = lst2.next
            pt = pt.next
        pt.next = lst1 if not lst2 else lst2
        return dummy.next
        
    
    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]
    mid = len(lists)/2
    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])

    return merge(left, right)

import heapq
def mergeKLists1(lists):
        
    ret, heap = [], []
    for lst in lists:
        while lst:
            heapq.heappush(heap, lst.val)
            print heap
            lst = lst.next

    while heap:
        ret.append(heapq.heappop(heap))
    return ret

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    
    print mergeKLists([list1, list2])	# Output 1 -> 2 -> 3 -> 4 -> None
    print mergeKLists1([list1, list2])	# Output [1, 2, 3, 4]
