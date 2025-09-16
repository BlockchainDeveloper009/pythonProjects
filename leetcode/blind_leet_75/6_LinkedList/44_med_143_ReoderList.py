class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorderList(head: ListNode) -> None:
    if not head or not head.next:
        return

    # Step 1: Find the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2: Reverse the second half
    prev, curr = None, slow.next
    slow.next = None  # split list into two
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp

    # Step 3: Merge two halves
    first, second = head, prev
    while second:
        temp1 = first.next
        temp2 = second.next

        first.next = second
        second.next = temp1

        first = temp1
        second = temp2



#Helper Functions (Build and Print Lists)
def build_list(arr):
    dummy = ListNode()
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


head = build_list([1,2,3,4])
reorderList(head)
print_list(head)  # Output: [1,4,2,3]

head2 = build_list([1,2,3,4,5])
reorderList(head2)
print_list(head2)  # Output: [1,5,2,4,3]


"""
143. Reorder List
Medium
Topics
premium lock iconCompanies

You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:

Input: head = [1,2,3,4]
Output: [1,4,2,3]

Example 2:

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]



Constraints:

    The number of nodes in the list is in the range [1, 5 * 104].
    1 <= Node.val <= 1000


"""

"""
The problem **Reorder List** can be solved in three main steps:

1. **Find the middle of the list** using the slow and fast pointer technique.
2. **Reverse the second half** of the list.
3. **Merge the two halves** by alternating nodes.

***

## Step-by-step Approach

### 1. Find the Middle
- Use two pointers `slow` and `fast`.
- `slow` moves one step, `fast` moves two steps.
- When `fast` reaches the end, `slow` is at the middle.

### 2. Reverse the Second Half
- Reverse the list starting from `slow.next`.
- Set `slow.next = None` to split the list.

### 3. Merge Two Lists
- Merge the first half and reversed second half alternating nodes.

***

## Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head: ListNode) -> None:
    if not head or not head.next:
        return
    
    # Step 1: Find the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    prev, curr = None, slow.next
    slow.next = None  # split list into two
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    
    # Step 3: Merge two halves
    first, second = head, prev
    while second:
        temp1 = first.next
        temp2 = second.next
        
        first.next = second
        second.next = temp1
        
        first = temp1
        second = temp2
```

***

## Helper Functions (Build and Print Lists)

```python
def build_list(arr):
    dummy = ListNode()
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
head = build_list([1,2,3,4])
reorderList(head)
print_list(head)  # Output: [1,4,2,3]

head2 = build_list([1,2,3,4,5])
reorderList(head2)
print_list(head2)  # Output: [1,5,2,4,3]
```

***

## Explanation

- Middle found splits list into two halves.
- Second half reversed for easy merging.
- Alternate nodes to reorder list as required.
- No node values are changed, only pointers.

***

## Complexity

- Time: $$O(n)$$, single passes on the list.
- Space: $$O(1)$$, in-place reordering without extra data structures.

***

**Summary:**  
Reorder list by splitting, reversing second half, and merging alternating nodes. This efficient approach modifies pointers in-place with linear time and constant space.[1][2]

[1](https://neetcode.io/problems/clone-graph)
[2](https://algo.monster/liteproblems/133)
"""