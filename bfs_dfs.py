

# Graph represented using an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
from collections import deque
# BFS Traversal
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # Add connected nodes to queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)


# DFS Traversal
def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()

    # Visit current node
    print(node, end=" ")
    visited.add(node)

    # Visit connected nodes recursively
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


print("BFS Traversal:")
bfs(graph, 'A')

print("\nDFS Traversal:")
dfs(graph, 'A')