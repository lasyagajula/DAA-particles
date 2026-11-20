
from itertools import permutations

n = 4

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

cities = range(1, n)

min_cost = float('inf')
best_path = []

for p in permutations(cities):
    path = (0,) + p + (0,)
    total = 0

    for i in range(len(path) - 1):
        total += cost[path[i]][path[i+1]]

    if total < min_cost:
        min_cost = total
        best_path = path

print("Minimum Cost:", min_cost)
print("Best Path:", best_path)
