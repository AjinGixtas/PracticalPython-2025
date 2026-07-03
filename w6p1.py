with open("w6p1.inp", "r", encoding="utf-8") as f: data = f.readlines()
lines = data[0].strip().split(" ")
uWs = []
for uW in lines: uWs.append([int(x) for x in uW.replace("(", "").replace(")", "").split(",")])
lines = data[1:]
kWs = []
for kW in lines:
    kW = kW.strip().replace("Cosmic", "C").replace("Solar", "S").split(",")
    kWs.append([int(kW[0]), int(kW[1]), kW[2]])
ans = ""
for uW in uWs:
    distD = []
    for i in range(len(kWs)):
        kW = kWs[i]
        dist = ((uW[0] - kW[0]) ** 2 + (uW[1] - kW[1]) ** 2) ** .5
        distD.append((dist, i))
    distD.sort(key=lambda x: x[0])
    S, C = 0, 0
    for i in range(min(len(distD), 7)):
        if kWs[distD[i][1]][2] == "S": S += 1
        else: C += 1
    ans += "S" if S > C else "C"
print(ans)