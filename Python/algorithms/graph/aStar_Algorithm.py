import heapq


def astar(start, goal, graph):
    frontier = [(0, start)]
    came_from = {}
    cost_so_far = {start: 0}

    while frontier:
        current_cost, current_node = heapq.heappop(frontier)

        if current_cost == goal:
            break

        for neighbor, cost in graph[current_node].items():
            new_cost = cost_so_far[current_node] + cost
            if (neighbor not in cost_so_far) or (new_cost < cost_so_far[neighbor]):
                cost_so_far[neighbor] = new_cost
                priority = new_cost + heuristic(neighbor, goal)
                heapq.heappush(frontier, (priority, neighbor))
                came_from[neighbor] = current_node

    path = []
    current_node = goal
    while current_node != start:
        path.append(current_node)
        current_node = came_from[current_node]
    path.append(start)
    path.reverse()

    return path, cost_so_far[goal]


def heuristic(node, goal):
    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def calculate_heuristic(cell):
    heuristic_values = {'A': 5, 'B': 3}
    return heuristic_values[cell]


# Example usage
graph = {
    (0, 0): {(0, 1): 1, (1, 0): 1},
    (0, 1): {(0, 0): 1, (1, 1): 1},
    (1, 0): {(0, 0): 1, (1, 1): 1},
    (1, 1): {(0, 1): 1, (1, 0): 1},
}
start = (0, 0)
goal = (1, 1)

path, cost = astar(start, goal, graph)

print("Shortest path: ", path)
print("Total cost: ", cost)
print(type(graph))
