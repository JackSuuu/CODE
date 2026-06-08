

# 如何使用邻接矩阵表示一个无向图
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, source, destination):
        # 无向图，连接是双向的
        self.matrix[source][destination] = 1
        self.matrix[destination][source] = 1

    def print_graph(self):
        for row in self.matrix:
            print(row)


# 创建一个包含 5 个节点的图
graph = Graph(5)
graph.add_edge(0, 1)
graph.add_edge(0, 4)
graph.add_edge(1, 2)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 4)

graph.print_graph()