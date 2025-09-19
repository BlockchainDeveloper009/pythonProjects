class ListNode:
    # Definition for singly-linked list node.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    """
    Detects if a linked list has a cycle using Floyd’s cycle detection algorithm.
    Uses two pointers moving at different speeds.
    """
    slow, fast = head, head  # Initialize two pointers both at head
    while fast and fast.next:
        slow = slow.next          # Move slow pointer by 1 step
        fast = fast.next.next     # Move fast pointer by 2 steps

        # If slow and fast meet, there is a cycle
        if slow == fast:
            return True

    # If fast reaches the end, no cycle in the list
    return False



# Helper to build a cycle linked list for testing
def build_cycle_list(values, pos):
    """
    Builds a linked list from 'values' with an optional cycle.

    Args:
        values: List of node values.
        pos: Position (0-index) where tail connects to form a cycle.
             If pos is -1, no cycle is added.

    Returns:
        Head of the constructed linked list.
    """
    # Create nodes for all values
    nodes = [ListNode(v) for v in values]

    # Link nodes in sequence
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # If pos is valid, link last node to node at position pos to form cycle
    if pos != -1 and nodes:
        nodes[-1].next = nodes[pos]

    # Return head of the linked list (first node), or None if empty list
    return nodes[0] if nodes else None

# --- Testing ---

# Test case 1:
# List: 3 -> 2 -> 0 -> -4
# Cycle: tail connects to node at index 1 (value 2)
head1 = build_cycle_list([3, 2, 0, -4], 1)
print(hasCycle(head1))  # Expected output: True (cycle present)

head3 = build_cycle_list([1], -1)        # no cycle
print(hasCycle(head3))  # False
# Test case 2:
# List: 1 -> 2
# Cycle: tail connects back to node at index 0 (value 1)
head2 = build_cycle_list([1, 2], 0)
print(hasCycle(head2))  # Expected output: True (cycle present)

# Test case 3:
# List: 1 (single node)
# Cycle: no cycle (pos = -1)
head3 = build_cycle_list([1], -1)
print(hasCycle(head3))  # Expected output: False (no cycle)

"""
141. Linked List Cycle
Easy
Topics
premium lock iconCompanies

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.



Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.



Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.



Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""

"""
The classic and optimal approach to detect a cycle in a linked list is **Floyd’s Cycle Detection Algorithm** (also known as the Tortoise and Hare algorithm). It uses two pointers moving at different speeds to determine if a cycle exists.

***

## Floyd’s Cycle Detection Algorithm (Tortoise and Hare)

- Use two pointers, `slow` and `fast`.
- `slow` moves one step at a time.
- `fast` moves two steps at a time.
- If there is no cycle, `fast` will reach the end (`None`).
- If there is a cycle, `slow` and `fast` will eventually meet inside the cycle.

***

## Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def hasCycle(head: ListNode) -> bool:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

***

## Explanation

- Both pointers start at the **head**.
- Move `slow` by one and `fast` by two nodes each loop iteration.
- If they meet, a cycle exists.
- If `fast` hits `None`, the list terminates with no cycle.

***

## Example Usage

```python
# Helper to build a cycle linked list for testing
def build_cycle_list(values, pos):
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0] if nodes else None

head1 = build_cycle_list([3,2,0,-4], 1)  # cycle linking to node with val=2
print(hasCycle(head1))  # True

head2 = build_cycle_list([1,2], 0)       # cycle linking to node with val=1
print(hasCycle(head2))  # True

head3 = build_cycle_list([1], -1)        # no cycle
print(hasCycle(head3))  # False
```

***

## Complexity

- Time: $$O(n)$$, each node visited maximum twice.
- Space: $$O(1)$$, uses only two pointers regardless of list size.

***

**Summary:**  
This approach efficiently detects cycles in linked lists with constant memory, making it the standard solution for this problem.[1][2][3][4][5]

[1](https://cp-algorithms.com/others/tortoise_and_hare.html)
[2](https://www.enjoyalgorithms.com/blog/detect-loop-in-linked-list/)
[3](https://takeuforward.org/data-structure/detect-a-cycle-in-a-linked-list/)
[4](https://www.interviewbit.com/blog/detect-loop-in-linked-list/)
[5](https://www.geeksforgeeks.org/dsa/detect-loop-in-a-linked-list/)
[6](https://leetcode.com/problems/linked-list-cycle/)
[7](https://stackoverflow.com/questions/2663115/how-to-detect-a-loop-in-a-linked-list)
[8](https://neetcode.io/problems/linked-list-cycle-detection?list=neetcode150)
[9](https://www.youtube.com/watch?v=wiOo4DC5GGA)
"""