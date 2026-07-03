morse = {'A':'._','B':'_...','C':'_._.','D':'_..','E':'.','F':'.._.','G':'__.','H':'....','I':'..','J':'.___','K':'_._','L':'._..','M':'__','N':'_.','O':'___','P':'.__.','Q':'__._','R':'._.','S':'...','T':'_','U':'.._','V':'..._','W':'.__','X':'_.._','Y':'_.__','Z':'__..','.':'._._._','?':'..__..','!':'_._.__','-':'_...._'}
reverse_morse = {v: k for k, v in morse.items()}
with open("w1p2.inp", "r", encoding="utf-8") as f: input = f.readlines()
S2 = ""
for c in input[0].strip():
    s1 = str(ord(c))
    S2 += s1
S2 = int(S2)
S3 = bin(S2)[2:].replace("1", "_").replace("0", ".")
S4 = S3.split(morse['!'])
print(S4)
ans = ""
for s4 in S4:
    if s4 == '': continue
    ans += reverse_morse[s4]
print(ans)