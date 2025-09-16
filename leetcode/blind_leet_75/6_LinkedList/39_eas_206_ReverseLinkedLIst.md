Here are **iterative** and **recursive** solutions to reverse a singly linked list (Leetcode 206).

***

## Linked List Node Definition

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

***

## Iterative Solution

```python
def reverseListIterative(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        next_node = current.next  # store next node
        current.next = prev       # reverse current node's pointer
        prev = current            # move prev forward
        current = next_node       # move current forward

    return prev
```

***

## Recursive Solution

```python
def reverseListRecursive(head: ListNode) -> ListNode:
    if not head or not head.next:
        return head

    new_head = reverseListRecursive(head.next)
    head.next.next = head
    head.next = None
    return new_head
```

***

## Explanation

- **Iterative:**
  - Move through list, reverse pointers one by one.
  - Keeps track of previous node to reverse pointers.
- **Recursive:**
  - Recurse to the end, then reverse the pointers back on unwind.
  - Base case: empty or single node list.

***

## Test Case Helper Functions

```python
def build_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)
```

***

## Example Usage

```python
head = build_list([1,2,3,4,5])
reversed_head_iter = reverseListIterative(head)
print_list(reversed_head_iter)  # Output: [5,4,3,2,1]

head2 = build_list([1,2])
reversed_head_rec = reverseListRecursive(head2)
print_list(reversed_head_rec)   # Output: [2,1]
```

***

**Summary:**  
Both iterative and recursive methods accomplish reversing the linked list efficiently, with the iterative often preferred due to constant space and straightforward logic.Here are both iterative and recursive solutions in Python to reverse a singly linked list for LeetCode 206:[1][2]

```python
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
```

This covers both iterative and recursive approaches with test cases and helper functions.

[1](https://www.interviewcoder.co/leetcode-problems/minimum-window-substring)
[2](https://takeuforward.org/data-structure/minimum-window-substring)