from collections import Counter

with open("w6p2.inp", "r", encoding="utf-8") as f: data = f.readlines()
M, D, T, A, R = [float(x) for x in data[0].strip().split(",")]
lines = data[1:]
Q = []
for line in lines: Q.append([float(x) for x in line.strip().split(",")[:5]] + [line.strip().split(",")[5]])
distD = []
for i in range(len(Q)):
    m, d, t, a, r, n = Q[i]
    distSQRD = (M - m) ** 2 + (D - d) ** 2 + (T - t) ** 2 + (A - a) ** 2 + (R - r) ** 2
    distSQRT = distSQRD ** .5
    distD.append((distSQRT, i))
distD.sort(key=lambda x: x[0])

counts = Counter(Q[i[1]][5] for i in distD[:7])
V, F = counts.most_common(1)[0]
print(V)