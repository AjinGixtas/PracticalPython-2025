from functools import cmp_to_key
with open("w2p1.inp", "r", encoding="utf-8") as f: input = f.readlines()
page_data = []
for line in input:
    page_data.append(line.strip().split(','))
page_data = page_data[1:]
def compare(a, b):
    if int(a[1]) - int(b[1]) != 0: return int(a[1]) - int(b[1])
    if a[2] < b[2]: return -1
    if a[2] > b[2]: return 1
    return int(a[3]) - int(b[3])
    
page_data.sort(key=cmp_to_key(compare))
ans = ""
for pageD in page_data: ans += pageD[0][0]
print(ans)