"""
Graph Patterns: DFS/BFS + topological sort
"""
from collections import defaultdict, deque

def alienOrder(words):
    graph = defaultdict(list)
    indegree = {c: 0 for word in words for c in word}
    for i in range(len(words) - 1):
        print(graph)
        w1, w2 = words[i], words[i+1]
        for c1, c2 in zip(w1, w2):
            if c1 != c2:
                if c2 not in graph[c1]:
                    graph[c1].append(c2)
                    indegree[c2] += 1
                break
    queue = deque([c for c in indegree if indegree[c] == 0])
    print(queue)
    result = ''
    while queue:
        c = queue.popleft()
        result += c
        for neighbor in graph[c]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    return result if len(result) == len(indegree) else ''

# Test: ["wrt","wrf","er","ett","rftt"] -> "wertf"
print(alienOrder(words=["wrt","wrf","er","ett","rftt"]))