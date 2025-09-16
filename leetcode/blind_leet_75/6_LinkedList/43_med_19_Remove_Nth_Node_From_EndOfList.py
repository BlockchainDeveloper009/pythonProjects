
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = second = dummy

    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next

    # Remove nth node from end
    second.next = second.next.next

    return dummy.next

def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


head = build_list([1,2,3,4,5])
new_head = removeNthFromEnd(head, 2)
print_list(new_head)  # Output: [1,2,3,5]

head2 = build_list([1])
new_head2 = removeNthFromEnd(head2, 1)
print_list(new_head2)  # Output: []

head3 = build_list([1,2])
new_head3 = removeNthFromEnd(head3, 1)
print_list(new_head3)  # Output: [1]


"""
19. Remove Nth Node From End of List
Medium
Topics
premium lock iconCompanies
Hint

Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]



Constraints:

    The number of nodes in the list is sz.
    1 <= sz <= 30
    0 <= Node.val <= 100
    1 <= n <= sz

"""

"""
To remove the nth node from the end of a linked list, the optimal approach is to use two pointers with a fixed distance of n between them, allowing removal in one pass.

***

## Approach

1. Use a **dummy node** that points to the head to simplify edge cases.
2. Initialize two pointers, `first` and `second`, at the dummy.
3. Move `first` pointer n+1 steps ahead.
4. Move both pointers until `first` reaches the end.
5. `second` will be just before the node to remove.
6. Adjust `second.next` to skip the target node.
7. Return `dummy.next` (new head).

***

## Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = second = dummy

    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next

    # Remove nth node from end
    second.next = second.next.next

    return dummy.next
```

***

## Helper Functions

```python
def build_list(arr):
    dummy = ListNode()
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)
```

***

## Example Usage

```python
head = build_list([1,2,3,4,5])
new_head = removeNthFromEnd(head, 2)
print_list(new_head)  # Output: [1,2,3,5]

head2 = build_list([1])
new_head2 = removeNthFromEnd(head2, 1)
print_list(new_head2)  # Output: []

head3 = build_list([1,2])
new_head3 = removeNthFromEnd(head3, 1)
print_list(new_head3)  # Output: [1]
```

***

## Explanation

- The two-pointer technique ensures one pass.
- Dummy node removes edge cases (like head removal).
- `second.next` removal bypasses the target node.

***

## Complexity

- Time: $$O(n)$$, single traversal.
- Space: $$O(1)$$, constant extra space.

***

This is the standard, efficient one-pass solution to remove the nth node from the end.To remove the nth node from the end of a linked list efficiently, use a two-pointer approach with a dummy node:[1][2]

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    first = second = dummy

    # Move first pointer n+1 steps ahead
    for _ in range(n + 1):
        first = first.next

    # Move both pointers until first reaches end
    while first:
        first = first.next
        second = second.next

    # Remove nth node
    second.next = second.next.next

    return dummy.next

# Helper to build and print linked list
def build_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_list(head):
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)

# Example usage:
head = build_list([1,2,3,4,5])
result = removeNthFromEnd(head, 2)
print_list(result)  # Output: [1, 2, 3, 5]

head2 = build_list()
result2 = removeNthFromEnd(head2, 1)
print_list(result2)  # Output: []

head3 = build_list([1,2])
result3 = removeNthFromEnd(head3, 1)
print_list(result3)  # Output: 
```

This solves the problem in one pass with O(n) time and O(1) space using the two-pointer technique and a dummy node to simplify edge cases.

[1](https://neetcode.io/problems/clone-graph)
[2](https://algo.monster/liteproblems/133)
"""