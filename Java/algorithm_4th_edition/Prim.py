import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find_min_key(self, key, mstSet):
        min = float('inf')
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v
        return min_index

    # Prime algorithm main procedure
    def prim_mst(self):
        key = [float('inf')] * self.V
        mstSet = [False] * self.V
        parent = [None] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.find_min_key(key, mstSet)
            mstSet[u] = True

            for neighbor in self.graph:
                v = neighbor[1] if neighbor[0] == u else neighbor[0]
                if self.graph[u][v] != 0 and mstSet[v] == False and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.print_mst(parent)

    def print_mst(self, parent):
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

# 客户端代码
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 2)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 8)
    g.add_edge(2, 3, 7)

    print("Following are the edges in the constructed MST")
    g.prim_mst()