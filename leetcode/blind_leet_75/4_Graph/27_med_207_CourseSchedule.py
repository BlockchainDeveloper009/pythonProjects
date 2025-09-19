
from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree =  * numCourses
    for a, b in prerequisites:        # b -> a (to take 'a', need 'b' first)
        graph[b].append(a)
        in_degree[a] += 1

    q = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited = 0

    while q:
        node = q.popleft()
        visited += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    # If every course was processed, no cycles (return True)
    return visited == numCourses


"""
207. Course Schedule
Medium
Topics
premium lock iconCompanies
Hint

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

    For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.



Constraints:

    1 <= numCourses <= 2000
    0 <= prerequisites.length <= 5000
    prerequisites[i].length == 2
    0 <= ai, bi < numCourses
    All the pairs prerequisites[i] are unique.


"""


""""
This problem is a standard **cycle detection in a directed graph**, often solved with **Topological Sort** (Kahn’s algorithm using BFS) or **DFS cycle detection**.  
The goal: If the course dependency graph has **no cycles**, all courses can be completed.[1][2]

***

## Kahn’s Algorithm (BFS Topological Sort) Solution

```python
from collections import deque, defaultdict

def canFinish(numCourses, prerequisites):
    graph = defaultdict(list)
    in_degree =  * numCourses
    for a, b in prerequisites:        # b -> a (to take 'a', need 'b' first)
        graph[b].append(a)
        in_degree[a] += 1

    q = deque([i for i in range(numCourses) if in_degree[i] == 0])
    visited = 0

    while q:
        node = q.popleft()
        visited += 1
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                q.append(neighbor)

    # If every course was processed, no cycles (return True)
    return visited == numCourses
```
- Build the graph, track incoming edges for every course.
- Courses with no prerequisites are added to queue.
- For each taken course, reduce in-degree of its dependents.
- If all courses are processed (`visited == numCourses`), it’s possible.

***

## DFS Cycle Detection (Alternative)

```python
def canFinish(numCourses, prerequisites):
    graph = [[] for _ in range(numCourses)]
    for a, b in prerequisites:
        graph[b].append(a)
    visited =  * numCourses   # 0=unvisited, 1=visiting, 2=visited

    def dfs(v):
        if visited[v] == 1:
            return False         # found cycle
        if visited[v] == 2:
            return True
        visited[v] = 1
        for u in graph[v]:
            if not dfs(u):
                return False
        visited[v] = 2
        return True

    for i in range(numCourses):
        if not dfs(i):
            return False
    return True
```
- Visit each node; mark “visiting” during recursion.
- If a node is revisited while “visiting”, a cycle exists.
- “visited=2” marks finished nodes.

***

## Example Testcases

```python
print(canFinish(2, [[1,0]]))             # True
print(canFinish(2, [[1,0],[0,1]]))       # False
print(canFinish(4, [[1,0],[2,1],[3,2]])) # True
print(canFinish(3, [[1,0],[0,2],[2,1]])) # False (cycle)
```

***

## DP/Graph Problem Type

| Problem                | Approach          | State/DP Type      | Output       |
|------------------------|-------------------|--------------------|--------------|
| Course Schedule (207)  | Topo Sort / DFS   | Graph/cycle detect | True/False   |

***

**Summary:**  
Detect cycles in the course prerequisite graph using **topological sort** or **DFS**.  
No cycles means all courses can be completed.[2][1]

[1](https://algo.monster/liteproblems/133)
[2](https://neetcode.io/problems/clone-graph)
"""