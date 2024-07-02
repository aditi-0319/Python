import heapq


def distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5


def heuristic_cost_estimate(path, cities):
    """Calculate the heuristic cost estimate for the given path."""
    if len(path) == 0:
        return 0
    return distance(cities[path[-1]], cities[path[0]])


def total_distance(path, cities):
    """Calculate the total distance of a path."""
    dist = 0
    for i in range(len(path)):
        dist += distance(cities[path[i]], cities[path[(i + 1) % len(path)]])
    return dist


def tsp_a_star(cities):
    """Solve TSP using A* algorithm."""
    num_cities = len(cities)
    start_node = ((), tuple(range(num_cities)))
    open_set = [(heuristic_cost_estimate(start_node[1], cities), start_node)]
    closed_set = set()

    while open_set:
        _, current_node = heapq.heappop(open_set)
        current_path = current_node[1]
        current_cost = total_distance(current_path, cities)

        if len(current_path) == num_cities:
            return current_cost, current_path

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for i in range(num_cities):
            if i not in current_path:
                neighbor_path = current_path + (i,)
                neighbor_node = (
                heuristic_cost_estimate(neighbor_path, cities) + total_distance(neighbor_path, cities), neighbor_path)
                heapq.heappush(open_set, neighbor_node)

    return float('inf'), None


# Example usage:
cities = [(0, 0), (1, 2), (3, 1), (2, 3)]
min_dist, best_path = tsp_a_star(cities)
print("Minimum distance:", min_dist)
print("Best path:", best_path)
