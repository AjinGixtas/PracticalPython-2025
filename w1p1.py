morse = {'A':'._','B':'_...','C':'_._.','D':'_..','E':'.','F':'.._.','G':'__.','H':'....','I':'..','J':'.___','K':'_._','L':'._..','M':'__','N':'_.','O':'___','P':'.__.','Q':'__._','R':'._.','S':'...','T':'_','U':'.._','V':'..._','W':'.__','X':'_.._','Y':'_.__','Z':'__..','.':'._._._','?':'..__..','!':'_._.__','-':'_...._'}
reverse_morse = {v: k for k, v in morse.items()}
with open("w1p1.inp", "r", encoding="utf-8") as f: input = f.readlines()
for line in input:
    letters = line.strip().split(" ")
    output = ""
    for letter in letters:
        output += reverse_morse[letter]
    print(output)