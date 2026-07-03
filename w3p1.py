with open("w3p1.inp", "r", encoding="utf-8") as f: input = f.readlines()
arm_index = int(input[0])
instructions = input[1].strip().split(",")
layout = input[2:]
for i in range(len(layout)):
    row = layout[i].strip()
    layout[i] = [] if row == "" else row.split(",")
tube = []
for i in range(len(instructions)):
    cmd = instructions[i][0]
    val = int(instructions[i][1:])
    if cmd == "L": 
        arm_index = arm_index - val
        continue
    if cmd == "R": 
        arm_index = arm_index + val
        continue
    if cmd == "T":
        idx = 0
        while idx < val:
            box = layout[arm_index].pop(0) if len(layout[arm_index]) > 0 else " "
            tube.insert(0, box)
            idx += 1
        continue
    if cmd == "D":
        idx = 0
        while idx < val:
            box = tube.pop() if len(tube) > 0 else " "
            layout[arm_index].append(box)
            idx += 1
        continue
ans = ""
for i in range(len(layout)):
    ans += layout[i][0] if len(layout[i]) != 0 else " "
    print(layout[i])
print(ans)