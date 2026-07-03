from collections import defaultdict, deque
# -- START -- Copied from ChatGPT ✌️
class Edge:
    def __init__(self, to, capacity):
        self.to = to
        self.capacity = capacity
        self.rev = None

class Dinic:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, capacity):
        forward = Edge(v, capacity)
        backward = Edge(u, 0)
        forward.rev = backward
        backward.rev = forward
        self.graph[u].append(forward)
        self.graph[v].append(backward)

    def bfs(self, source, sink):
        self.level = {}
        q = deque([source])
        self.level[source] = 0
        while q:
            u = q.popleft()
            for edge in self.graph[u]:
                if (edge.capacity > 0 and edge.to not in self.level):
                    self.level[edge.to] = (self.level[u] + 1)
                    q.append(edge.to)
        return sink in self.level

    def dfs(self, u, sink, flow):
        if u == sink: return flow
        edges = self.graph[u]
        while self.ptr[u] < len(edges):
            edge = edges[self.ptr[u]]
            if (edge.capacity > 0 and self.level.get(edge.to, -1) == self.level[u] + 1):
                pushed = self.dfs(edge.to, sink, min(flow, edge.capacity))
                if pushed > 0:
                    edge.capacity -= pushed
                    edge.rev.capacity += pushed
                    return pushed
            self.ptr[u] += 1
        return 0

    def max_flow(self, source, sink):
        total = 0
        while self.bfs(source, sink):
            self.ptr = defaultdict(int)
            while True:
                pushed = self.dfs(source, sink, float("inf"))
                if pushed == 0: break
                total += pushed
        return total
# --- END --- Copied from ChatGPT ✌️

with open("w10p1.inp", "r", encoding="utf-8") as f: data = f.readlines()
graph = Dinic()
for line in data:
    parts = line.strip().split(" ")
    capacity = int(parts[1])
    nodes = parts[0].split("-")
    start = nodes[0]
    end = nodes[1]
    graph.add_edge(start, end, capacity)
print(graph.max_flow("S1", "MD"))