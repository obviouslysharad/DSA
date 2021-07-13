import heapq

def findMin(graph, root):
    minDistanceGraph = {}
    for i in graph:
        minDistanceGraph[i] = 1000
    
    minDistanceGraph[root] = 0

    pq = [(root, 0)]

    while len(pq) > 0:

        current_node, current_distance = heapq.heappop(pq)

        for neighour, distance in graph[current_node].items():
            distance = distance + current_distance
            if distance < minDistanceGraph[neighour]:
                 minDistanceGraph[neighour] = distance
                 heapq.heappush(pq, (neighour, distance))

    return minDistanceGraph

graph = {
    'A' : {'B': 2, 'C': 5, 'D': 2, 'E': 7, 'F': 50},
    'B' : {'C': 2, 'D': 1, 'E': 2, 'F': 60},
    'C' : {'B': 3, 'E': 2, 'F':90},
    'D' : {'E': 1, 'F': 3}, 
    'E' : {'D': 4, 'F': 4},
    'F' : {}
} 

print(findMin(graph, 'A'))