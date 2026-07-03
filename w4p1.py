import re
with open("w4p1.inp", "r", encoding="utf-8") as f: input = f.readlines()
X, Y = "", ""
for i in range(len(input)):
    specimens = input[i].strip().split(" ")
    D = []
    for j in range(len(specimens)):
        profile = re.split("[(),]", specimens[j])
        D.append([int(x) for x in profile[:3]])
    x = (D[0][0] * D[0][1] + D[1][0] * D[1][1] + D[2][0] * D[2][1]) / (D[0][0] + D[1][0] + D[2][0])
    y = (D[0][0] * D[0][2] + D[1][0] * D[1][2] + D[2][0] * D[2][2]) / (D[0][0] + D[1][0] + D[2][0])
    X += chr(int(x))
    Y += chr(int(y))
ans = X + " " + Y
print(ans)