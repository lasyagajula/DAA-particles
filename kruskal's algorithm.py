def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)

    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1


def kruskal(graph, vertices):
    result = []
    graph.sort(key=lambda x: x[2])

    parent = []
    rank = []

    for i in range(vertices):
        parent.append(i)
        rank.append(0)

    for u, v, weight in graph:
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append((u, v, weight))
            union(parent, rank, x, y)

    print("Edges in Minimum Spanning Tree:")
    total = 0

    for u, v, weight in result:
        print(u, "-", v, ":", weight)
        total += weight

    print("Minimum Cost:", total)


graph = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

kruskal(graph, 4)
