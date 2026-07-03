from collections import deque
with open("w4p2.inp", "r", encoding="utf-8") as f: data = [list(map(int, line.strip().split(","))) for line in f if line.strip()]
bmap = [[0] * len(data[0]) for _ in range(len(data))]

def calculate_cluster(y, x):
    DIRECTION = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(y, x)])
    M = 0
    M_x = 0
    M_y = 0
    while queue:
        y, x = queue.popleft()
        if y < 0 or y >= len(data): continue
        if x < 0 or x >= len(data[y]): continue
        if data[y][x] == 0: continue
        if bmap[y][x] != 0: continue
        bmap[y][x] = 1
        val = data[y][x]
        M += val
        M_x += val * x
        M_y += val * y
        for dy, dx in DIRECTION: queue.append((y + dy, x + dx))
    return (M, M_x // M, M_y // M)
ans = (0, 0, 0)
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0: continue
        if bmap[y][x] != 0: continue
        cluster_data = calculate_cluster(y, x)
        found = True
        if cluster_data[0] > ans[0]: ans = cluster_data
print(ans)