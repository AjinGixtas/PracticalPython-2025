from collections import defaultdict

with open("w8p1.inp", "r", encoding="utf-8") as f: items = f.readlines()[1:]
W = 300

for i in range(len(items)):
    items[i] = items[i].strip().split(",")
    items[i][3] = int(items[i][3])
    items[i][4] = int(items[i][4])
all_types = sorted(set(x[2] for x in items))
type_to_bit = { t: i for i, t in enumerate(all_types) }
FULL_MASK = (1 << len(all_types)) - 1

groups = defaultdict(list)
for item in items: groups[item[1]].append(item)

dp = [[-float('inf')] * (FULL_MASK + 1) for _ in range(W + 1)]


dp[0][0] = 0
for enumA, choices in groups.items():
    new_dp = [row[:] for row in dp]

    for item in choices:
        idx, _, enumB, weight, value = item
        bit = 1 << type_to_bit[enumB]

        for cap in range(W - weight, -1, -1):
            for mask in range(FULL_MASK + 1):

                if dp[cap][mask] == -float('inf'): continue

                new_mask = mask | bit
                new_dp[cap + weight][new_mask] = max(
                    new_dp[cap + weight][new_mask],
                    dp[cap][mask] + value
                )
    dp = new_dp

best = max(dp[cap][FULL_MASK] for cap in range(W + 1))
print(best)