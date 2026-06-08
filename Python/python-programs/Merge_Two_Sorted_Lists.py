# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Creating nodes with value 1, 2, 4
l1_node1 = ListNode(1)
l1_node2 = ListNode(2)
l1_node3 = ListNode(3)

# Linking node together
l1_node1.next = l1_node2
l1_node2.next = l1_node3


def mergeTwoLists(self, list1: ListNode, list2: ListNode):
    cur = dummy = ListNode()

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            # list1, cur = list1.next, list1
            cur = cur.next; list1 = list1.next
        else:
            cur.next = list2
            # list2, cur = list2.next, list2
            cur = cur.next; list2 = list2.next
    
    if list1 or list2:
        cur.next = list1 if list1 else list2

    return dummy.next