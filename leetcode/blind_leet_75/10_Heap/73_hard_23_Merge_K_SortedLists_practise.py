import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    min_heap = []

    # Build initial heap (value, index, node) for stable sorting
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))

    dummy = ListNode()
    current = dummy

    while min_heap:
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))

    return dummy.next

def mergeUnsortedLists(lists):
    min_heap = []
    
    # 1. Push EVERY single node from every list into the heap
    for node in lists:
        while node:
            # We use id(node) as a tie-breaker so Python doesn't compare node objects
            heapq.heappush(min_heap, (node.val, id(node), node))
            node = node.next
            
    dummy = ListNode()
    current = dummy
    
    # 2. Pop them out. They will naturally come out in perfectly sorted order.
    while min_heap:
        val, _, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        
    current.next = None # Clear the final pointer
    return dummy.next


# Helper to build linked list from Python list
def build_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Input lists [[1,4,5],[1,3,4],[2,6]]
lists = [
    build_linked_list([1,4,5]),
    build_linked_list([1,3,4]),
    build_linked_list([2,6])
]

merged_head = mergeKLists(lists)

# Helper to print linked list
def print_linked_list(node):
    arr = []
    while node:
        arr.append(str(node.val))
        node = node.next
    print("->".join(arr))

print_linked_list(merged_head)  # Output: 1->1->2->3->4->4->5->6



"""

23. Merge k Sorted Lists
Hard
Topics
premium lock iconCompanies

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []



Constraints:

    k == lists.length
    0 <= k <= 104
    0 <= lists[i].length <= 500
    -104 <= lists[i][j] <= 104
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 104.


"""



steup live sessions
career coaching session,
mockup
student associate.

transition:::

program advisor ->

devik.kaul@interviewkickstart.com

