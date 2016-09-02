'''
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        lst = []

        while cur is not None:
            lst.insert(0, cur)
            cur = cur.next

        removed_node = lst[n - 1]
        if n == len(lst):
            return head.next
        prev_node = lst[n]
        if n <= 1:
            next_node = None
        else:
            next_node = lst[n - 2]

        prev_node.next = next_node
        removed_node.next = None
        return head

test_list = [1, 2, 3]

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

head = Solution().removeNthFromEnd(head, 2)
cur = head
while cur is not None:
    print cur.val,
    cur = cur.next
