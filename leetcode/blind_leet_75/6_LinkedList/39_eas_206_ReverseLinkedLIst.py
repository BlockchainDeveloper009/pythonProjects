# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode])
#         -> Optional[ListNode]:
#
#

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative method
def reverseListIterative(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # store next
        curr.next = prev       # reverse pointer
        prev = curr            # move prev
        curr = next_node       # move curr
    return prev

# Recursive method
def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head
    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head

# Helper to build linked list from list
def build_list(arr):
    dummy = ListNode()
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

# Helper to print linked list as list
def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)

# Testing
head = build_list([1,2,3,4,5])
rev_iter = reverseListIterative(head)
print_list(rev_iter)  # [5,4,3,2,1]

head2 = build_list([1,2])
rev_rec = reverseListRecursive(head2)
print_list(rev_rec)   # [2,1]



"""
206. Reverse Linked List
Easy
Topics
premium lock iconCompanies

Given the head of a singly linked list, reverse the list, and return the reversed list.



Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []



Constraints:

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000



Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

"""

