from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)  # Dictionary to store edges (vertex -> list of neighbors)

    def add_edge(self, u, v):
        self.graph[u].append(v)  # Add edge from u to v

    def topological_sort(self):
        # Set to keep track of visited vertices
        visited = set()
        # List to store the topological order
        order = []

        # DFS helper function
        def dfs(vertex):
            # Mark the current vertex as visited
            visited.add(vertex)
            # Explore all neighbors
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs(neighbor)
            # After exploring all neighbors, add vertex to the order
            order.append(vertex)

        # Collect all vertices before iterating to avoid modifying defaultdict
        vertices = list(self.graph.keys())
        # Run DFS on all vertices to handle disconnected components
        for vertex in vertices:
            if vertex not in visited:
                dfs(vertex)

        # Reverse the order to get the topological sort
        return order[::-1]

# Example usage
g = Graph()
g.add_edge(5, 2)  # 5 must come before 2
g.add_edge(5, 0)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)

print("Topological Sort:", g.topological_sort())