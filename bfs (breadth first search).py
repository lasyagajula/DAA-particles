
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)

            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    queue.append(neighbour)

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS Traversal:")
bfs(graph, 'A')
