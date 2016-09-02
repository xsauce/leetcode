# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_head = new_cur = ListNode('')
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                new_cur.next = l1
                l1 = l1.next
            else:
                new_cur.next = l2
                l2 = l2.next
            new_cur = new_cur.next

        if l1 is None and l2 is not None:
            new_cur.next = l2
        if l2 is None and l1 is not None:
            new_cur.next = l1

        return new_head.next


def init_list_node(test_list):
    cur = None
    head = None
    for i in test_list:
        if cur is None:
            cur = ListNode(i)
            head = cur
        else:
            next = ListNode(i)
            cur.next = next
            cur = next
    return head

def print_list_node(head):
    cur = head
    while cur is not None:
        print cur.val
        cur = cur.next



s = Solution()
head = s.mergeTwoLists(
    init_list_node([]),
    init_list_node([2])
)

print_list_node(head)