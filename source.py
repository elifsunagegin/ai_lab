import heapq
from collections import deque

# Distance matrix between cities
cities = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

def bfs_tsp(cities, start):
    # Initialize a queue for BFS
    queue = deque([(start, [start], 0)])
    min_cost = float('inf')  # Initialize minimum cost to infinity
    best_path = None

    # Start BFS traversal
    while queue:
        current_city, path, total_cost = queue.popleft()

        # If all cities are visited, return to the start city
        if len(path) == len(cities):
            total_cost += cities[current_city][start]  # Add cost to return to start city
            if total_cost < min_cost:
                min_cost = total_cost
                best_path = path + [start]  # Update best path with return to start city
        else:
            # Explore neighbors of the current city
            for neighbor, cost in cities[current_city].items():
                if neighbor not in path:  # Check if neighbor is not visited yet
                    queue.append((neighbor, path + [neighbor], total_cost + cost))  # Enqueue neighbor for traversal

    return best_path, min_cost

# Run the BFS algorithm
path, cost = bfs_tsp(cities, 'A')
print("BFS Path:", path)
print("BFS Cost:", cost)