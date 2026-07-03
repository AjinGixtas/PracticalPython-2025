from functools import cmp_to_key
with open("w2p2.inp", "r", encoding="utf-8") as f: input = f.readlines()
braille = { 'A':'100000','B':'110000','C':'100100','D':'100110','E':'100010','F':'110100','G':'110110','H':'110010','I':'010100','J':'010110','K':'101000','L':'111000','M':'101100','N':'101110','O':'101010','P':'111100','Q':'111110','R':'111010','S':'011100','T':'011110','U':'101001','V':'111001','W':'010111','X':'101101','Y':'101111','Z':'101011',' ':'000000'}
reverse_braille = {v: k for k, v in braille.items()}
datas = []
for line in input:
    datas.append(line.strip().split(","))
datas.sort(key=lambda x: x[1])
P1, P2 = "", ""
for i in range(0, len(datas), 2):
    c1 = datas[i][0][:3] + datas[i+1][0][:3]
    c2 = datas[i][0][3:] + datas[i+1][0][3:]
    P1 += reverse_braille[c1]
    P2 += reverse_braille[c2]
print(P1 + P2)