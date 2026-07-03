with open("w8p1.inp", "r", encoding="utf-8") as f: data = f.readlines()[1:]
for i in range(len(data)):
    data[i] = data[i].strip().split(",")
    data[i][3] = int(data[i][3])
    data[i][4] = int(data[i][4])
def knapsack(weights, values, W):
    dp = [0] * (W + 1)
    for w, v in zip(weights, values):
        for c in range(W, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[W]
ans = knapsack([ data[i][3] for i in range(len(data)) ],[ data[i][4] for i in range(len(data)) ], 300)
print(ans)