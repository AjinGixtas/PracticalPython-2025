# Exact same as w9p1
from collections import deque
MAX = 1e10
with open("w9p2.inp", "r", encoding="utf-8") as f: data = f.readlines()

startID = int(data[0].strip().split(",")[0])
endID = int(data[0].strip().split(",")[1])
graph = {}
for i in range(1, len(data)):
    key = int(data[i].strip().split(":")[0])
    values_str = data[i].strip().split(":")[1].split(",")
    graph[key] = [int(e) for e in values_str]
def BFS(start, end, graph):
    checked = []
    queue = deque([start])
    node_dist = { start: 1 }
    while len(queue) > 0:
        current = queue.popleft()
        #print(f"CURR = {current}; QUEUE = {queue}; CHECKED = {checked}; NODE_DIST = {node_dist}; ENDED? = {current == end}; CHECKED? = {current in checked}")
        if current == end: return node_dist[end]
        if current in checked: continue
        neighbours = graph[current]
        checked.append(current)
        for neighbour in neighbours:
            node_dist[neighbour] = min(node_dist[current] + 1, node_dist.get(neighbour, MAX))
            queue.appendleft(neighbour)
    return "-1"
print(BFS(startID, endID, graph))
