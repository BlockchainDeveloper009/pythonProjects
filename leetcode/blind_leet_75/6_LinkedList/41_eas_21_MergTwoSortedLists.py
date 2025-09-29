class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes
    #current.next = list1 if list1 else list2
    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


def mergeTwoListsRecursive(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoListsRecursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoListsRecursive(list1, list2.next)
        return list2


def build_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    print(vals)


list1 = build_list([1,2,4])
list2 = build_list([1,3,4])

merged_iter = mergeTwoLists(list1, list2)
print_list(merged_iter)  # Output: [1,1,2,3,4,4]

# For recursive approach, rebuild lists because merged_iter has consumed them
list1 = build_list([1,2,4])
list2 = build_list([1,3,4])

merged_rec = mergeTwoListsRecursive(list1, list2)
print_list(merged_rec)  # Output: [1,1,2,3,4,4]


"""
21. Merge Two Sorted Lists
Easy
Topics
premium lock iconCompanies

You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]



Constraints:

    The number of nodes in both lists is in the range [0, 50].
    -100 <= Node.val <= 100
    Both list1 and list2 are sorted in non-decreasing order.


"""

"""
To merge two sorted linked lists into one sorted linked list, you can use a simple iterative or recursive approach. Below are both solutions with explanations.

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
def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # Attach remaining nodes
    current.next = list1 if list1 else list2

    return dummy.next
```

***

## Recursive Solution

```python
def mergeTwoListsRecursive(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    if not list2:
        return list1

    if list1.val < list2.val:
        list1.next = mergeTwoListsRecursive(list1.next, list2)
        return list1
    else:
        list2.next = mergeTwoListsRecursive(list1, list2.next)
        return list2
```

***

## Helper Functions (Build and Print Lists)

```python
def build_list(arr):
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
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
list1 = build_list([1,2,4])
list2 = build_list([1,3,4])

merged_iter = mergeTwoLists(list1, list2)
print_list(merged_iter)  # Output: [1,1,2,3,4,4]

# For recursive approach, rebuild lists because merged_iter has consumed them
list1 = build_list([1,2,4])
list2 = build_list([1,3,4])

merged_rec = mergeTwoListsRecursive(list1, list2)
print_list(merged_rec)  # Output: [1,1,2,3,4,4]
```

***

## Explanation

- **Iterative:** Use a dummy node and pointers; append smaller node each time.
- **Recursive:** Pick smaller head, recursively merge the rest.

***

## Complexity

- Time: $$O(n + m)$$, where $$n, m$$ are lengths of the lists.
- Space: $$O(1)$$ iterative, $$O(n+m)$$ recursive (due to call stack).

***

This completes efficient merging of two sorted linked lists using both iterative and recursive methods.
"""