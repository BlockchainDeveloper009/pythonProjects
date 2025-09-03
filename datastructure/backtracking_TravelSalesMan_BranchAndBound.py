import math

# Number of cities
N = 4

# Infinity-like large value for initial comparisons
maxsize = float('inf')

# Stores final optimal path found
final_path = [None] * (N + 1)

# Boolean list to track visited cities in current path
visited = [False] * N

# Stores minimum cost of shortest tour found so far
final_res = maxsize


def copy_to_final(curr_path):
    """
    Copies current path to final_path and completes cycle
    """
    for i in range(N):
        final_path[i] = curr_path[i]
    final_path[N] = curr_path[0]


def first_min(adj, i):
    """
    Returns minimum edge cost from city i to any other city
    """
    min_val = maxsize
    for k in range(N):
        if adj[i][k] < min_val and i != k:
            min_val = adj[i][k]
    return min_val


def second_min(adj, i):
    """
    Returns second minimum edge cost from city i to any other city
    """
    first, second = maxsize, maxsize
    for j in range(N):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif adj[i][j] <= second and adj[i][j] != first:
            second = adj[i][j]
    return second


def tsp_rec(adj, curr_bound, curr_weight, level, curr_path):
    """
    Recursive function to solve TSP using Branch and Bound
    Args:
        adj: adjacency matrix of city distances
        curr_bound: lower bound of path cost so far
        curr_weight: total weight/cost of current path so far
        level: current depth or number of cities visited
        curr_path: current path of cities visited
    """
    global final_res
    # Base case: if all cities are visited, check if last connects to start
    if level == N:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                copy_to_final(curr_path)
                final_res = curr_res
        return

    # Try to go to every city that is not visited yet
    for i in range(N):
        if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp = curr_bound
            curr_weight += adj[curr_path[level - 1]][i]

            # Compute new lower bound depending on level (special case for level 1)
            if level == 1:
                curr_bound -= (first_min(adj, curr_path[level - 1]) + first_min(adj, i)) / 2
            else:
                curr_bound -= (second_min(adj, curr_path[level - 1]) + first_min(adj, i)) / 2

            # If current lower bound + weight is better than final result, recurse deeper
            if curr_bound + curr_weight < final_res:
                curr_path[level] = i
                visited[i] = True
                tsp_rec(adj, curr_bound, curr_weight, level + 1, curr_path)

            # Backtrack: undo changes for curr_weight, curr_bound, and visited
            curr_weight -= adj[curr_path[level - 1]][i]
            curr_bound = temp
            visited[i] = False


def tsp(adj):
    """
    Setup and call recursive TSP solver
    """
    global final_res
    curr_bound = 0
    curr_path = [-1] * (N + 1)

    # Compute initial lower bound for root node
    for i in range(N):
        curr_bound += (first_min(adj, i) + second_min(adj, i))
    curr_bound = math.ceil(curr_bound / 2)

    visited[0] = True
    curr_path[0] = 0

    # Start recursion from first city
    tsp_rec(adj, curr_bound, 0, 1, curr_path)


# Example adjacency matrix of distances between 4 cities
adj = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

tsp(adj)

print(f"Minimum tour cost: {final_res}")
print("Path taken:", end=" ")
for city in final_path:
    print(city, end=" ")
print()
