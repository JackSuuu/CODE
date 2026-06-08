
# Construct the graph structure
# {'start': {'a': 6, 'b': 2}}
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

# for each in graph["start"].keys():
#     print(each)
#
# print(graph["start"]["a"])

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}


# Construct a table that contains the cost
# Set infinite value
infinity = float("inf")
cost_s = {}
cost_s["a"] = 6
cost_s["b"] = 2
cost_s["fin"] = infinity


# Construct a table that contains the Parents
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None


print(graph["start"].keys())
print(graph["start"]["a"])
print(cost_s)
print(parents)

# An array to stored marked node
processed = []


# The Implementation of the comprehensive process
def find_lowest_cost_node(costs):
    global processed
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


def output_result(par: dict):
    node = "fin"
    res = []
    result = ""
    for _ in par:
        res.append(par[node])
        node = par[node]
    for each in reversed(res):
        result += each + ' --> '
    result += "fin"
    print(result)


def Dijkstra():
    # 三个哈希表
    global graph, cost_s, parents
    # 找出开销最小的节点
    node = find_lowest_cost_node(cost_s)
    while node is not None:
        cost = cost_s[node]
        neighbors = graph[node]
        # 遍历当前节点的所有邻居
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            # 如果经当前节点前往该邻居更近
            if new_cost < cost_s[n]:
                # 更新邻居开销
                cost_s[n] = new_cost
                # 将邻居的父节点设置为当前节点
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(cost_s)


Dijkstra()
# print(parents)
print("==============================")
print("The final pathway is: ")
output_result(parents)
