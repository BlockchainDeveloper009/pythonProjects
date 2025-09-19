# Online Python Playground
# Use the online IDE to write, edit & run your Python code
# Create, edit & delete files online

from typing import List, Optional
import heapq

# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        # Heap requires nodes to be comparable
        return self.val < other.val
def build_linked_list(arr):
    """Builds a linked list from a Python list and returns the head node."""
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

def print_linked_list(head):
    """Prints ListNode linked list as a list."""
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    print(arr)

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Initialize a priority queue (min-heap)
        min_heap = []

        # Push the head of each list onto the heap (ignore empty lists)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, node)

        # Dummy node to simplify edge cases
        dummy = ListNode(0)
        current = dummy

        while min_heap:
            # Pop node with smallest value
            smallest = heapq.heappop(min_heap)
            current.next = smallest
            current = current.next

            # If there's a next node, push onto heap
            if smallest.next:
                heapq.heappush(min_heap, smallest.next)

        return dummy.next


lists1 = [[1,4,5],[1,3,4],[2,6]]

# Convert each list to a ListNode linked list
node_lists = [build_linked_list(lst) for lst in lists1]

s = Solution()
merged_head = s.mergeKLists(node_lists)
print_linked_list(merged_head)
print('----------')


lists2 = [[1,4,5],[1,3,4],[2,6],[3,8,9],[10,20]]

# Convert each list to a ListNode linked list
node_lists = [build_linked_list(lst) for lst in lists2]

s = Solution()
merged_head = s.mergeKLists(node_lists)
print_linked_list(merged_head)
print('----------')