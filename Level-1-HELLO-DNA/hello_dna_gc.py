print("Hello DNA 🧬")

dna = "ATGCGATATCGCG"
dna = dna.upper()

a = dna.count('A')
t = dna.count('T')
g = dna.count('G')
c = dna.count('C')
total = len(dna)
gc_percent = (g + c) / total * 100

print("Sequence:", dna)
print("Length:", total)
print("A:", a, " T:", t, " G:", g, " C:", c)
print(f"GC% = {gc_percent:.2f}%")
