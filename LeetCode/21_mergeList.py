class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def MergeSortedList(list1: ListNode, list2: ListNode):
    dummyHead = ListNode()
    curr_node = dummyHead
    l1 = list1
    l2 = list2

    while (l1 is not None) and (l2 is not None):
        if l1.val < l2.val:
            curr_node.next = l1
            l1 = l1.next
        else:
            curr_node.next = l2
            l2 = l2.next
        curr_node = curr_node.next
    
    if l1 is not None:
        curr_node.next = l1
    if l2 is not None:
        curr_node.next = l2
    
    return dummyHead.next