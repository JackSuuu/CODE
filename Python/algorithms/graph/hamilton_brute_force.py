# Hamiltonian Cycle using brute force approach

def hamiltonian_cycle(G, v1):
    # Start with one vertex in the path
    path_length = 1

    # Initialize visited array to False
    visited = [False] * len(G)

    # Start from vertex v1
    visited[v1] = True

    # Start recursion from v1
    return hamilton_from_vertex(G, v1, v1, path_length, visited)


def hamilton_from_vertex(G, w, v1, path_length, visited):
    # Base case: If all vertices are visited and there is an edge back to the start
    if path_length == len(G) and v1 in G[w]:
        return True  # Cycle found

    # If all vertices are visited but no edge back to the start
    elif path_length == len(G):
        return False  # Path is full, but no cycle

    # Explore neighbors of the current vertex
    for x in G[w]:
        if not visited[x]:
            # Mark the vertex as visited
            visited[x] = True
            path_length += 1

            # Recur for the next vertex
            if hamilton_from_vertex(G, x, v1, path_length, visited):
                return True

            # Backtrack
            visited[x] = False
            path_length -= 1

    return False


# Example usage:
# Graph represented as an adjacency list
graph = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2]
}

# Check if the graph has a Hamiltonian cycle starting from vertex 0
print(hamiltonian_cycle(graph, 0))  # Output: True or False