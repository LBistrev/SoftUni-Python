from queue import PriorityQueue
from collections import deque


class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


number_edges = int(input())
graph = {}

for _ in range(number_edges):
    source, destination, weight = [int(x) for x in input().split(', ')]
    if source not in graph:
        graph[source] = []
    if destination not in graph:
        graph[destination] = []

    graph[source].append(Edge(source, destination, weight))

start_node = int(input())
end_node = int(input())

max_node = max(graph.keys())

distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start_node] = 0

pq = PriorityQueue()
pq.put((0, start_node))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end_node:
        break
    for edge in graph[node]:
        new_distance = min_distance + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = node
            pq.put((new_distance, edge.destination))

if distance[end_node] == float('inf'):
    print('There is no such path.')
else:
    print(distance[end_node])

    path = deque()
    node = end_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')

# Examples
"""
    18
    0, 6, 10
    0, 8, 12
    6, 4, 17
    6, 5, 6
    8, 5, 3
    5, 4, 5
    5, 11, 33
    8, 2, 14
    2, 11, 9   -> 42
    2, 7, 15   -> 0 8 5 4 11 1 9
    4, 1, 20
    4, 11, 11
    11, 1, 6
    11, 7, 20
    1, 9, 5
    1, 7, 26
    7, 9, 3
    3, 10, 7
    0
    9

---------------------------

    18
    0, 6, 10
    0, 8, 12
    6, 4, 17
    6, 5, 6
    8, 5, 3
    5, 4, 5
    5, 11, 33
    8, 2, 14
    2, 11, 9
    2, 7, 15   ->  There is no such path.
    4, 1, 20
    4, 11, 11
    11, 1, 6
    11, 7, 20
    1, 9, 5
    1, 7, 26
    7, 9, 3
    3, 10, 7
    0
    10


"""
