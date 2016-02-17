# Definition for singly-linked list.
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        lr = None
        head = None
        carry_over = 0
        while l1 is not None or l2 is not None or carry_over != 0:
            tval = 0
            if l1 is None and l2 is not None:
                tval = l2.val
                l2 = l2.next
            if l1 is not None and l2 is None:
                tval = l1.val
                l1 = l1.next
            if l1 is not None and l2 is not None:
                tval = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            tval += carry_over
            if tval >= 10:
                carry_over = 1
                tval = tval % 10
            else:
                carry_over = 0
            if lr is None:
                head = lr = ListNode(tval)
            else:
                lr.next = ListNode(tval)
                lr = lr.next
        return head


def create_list(a):
    l1 = ListNode(a[0])
    temp = l1
    for i in a[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return l1


def print_list(a):
    while a is not None:
        print a.val,
        a = a.next
    print


if __name__ == '__main__':
    s = Solution()
    a = [5]
    b = [5]
    l1 = create_list(a)
    l2 = create_list(b)
    print_list(l1)
    print_list(l2)
    lr = s.addTwoNumbers(l1, l2)
    print_list(lr)
