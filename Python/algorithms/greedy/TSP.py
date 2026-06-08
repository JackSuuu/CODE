import math

def distance(point1, point2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def tsp_greedy(points):
    """
    Solve the Travelling Salesman Problem using a greedy algorithm.
    
    Args:
        points (list of tuples): List of coordinates representing the cities.
        
    Returns:
        list: The order of cities in the tour.
        float: The total distance of the tour.
    """
    n = len(points)
    if n == 0:
        return [], 0

    visited = [False] * n
    tour = []
    total_distance = 0

    # Start from the first city
    current_city = 0
    tour.append(current_city)
    visited[current_city] = True

    for _ in range(n - 1):
        nearest_city = None
        nearest_distance = float('inf')

        # Find the nearest unvisited city
        nearest_city, nearest_distance = min(
            ((next_city, distance(points[current_city], points[next_city])) 
             for next_city in range(n) if not visited[next_city]),
            key=lambda x: x[1]
        )

        # Visit the nearest city
        visited[nearest_city] = True
        tour.append(nearest_city)
        total_distance += nearest_distance
        current_city = nearest_city

    # Return to the starting city
    total_distance += distance(points[current_city], points[tour[0]])
    tour.append(tour[0])

    return tour, total_distance

# Example usage
if __name__ == "__main__":
    cities = [(0, 0), (2, 0), (2, 2), (0, 2)]
    tour, total_distance = tsp_greedy(cities)
    print("Tour:", tour)
    print("Total Distance:", total_distance)