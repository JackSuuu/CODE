from collections import deque

# Create graph using dictionary as adjacency list
graph = {
    "you": ["alice", "bob", "claire"],
    "alice": ["peggy"],
    "bob": ["anuj", "peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": []
}

print("Graph adjacency list:")
for vertex, neighbors in graph.items():
    print(f"{vertex}: {neighbors}")

# BFS is implemented using a deque (FIFO)
def BFS(target, root="you"):
    search_queue = deque()
    search_queue.extend(graph[root])
    # To avoid revisiting vertices
    searched = set()
    searched.add(root)
    
    # When the queue is not empty
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person == target:
                print(f"Target {person} found!")
                return True
            else:
                search_queue.extend(graph[person])
                searched.add(person)
    
    print(f"Target {target} not found")
    return False

print("\nRunning BFS:")
BFS(target="thom", root="you")
