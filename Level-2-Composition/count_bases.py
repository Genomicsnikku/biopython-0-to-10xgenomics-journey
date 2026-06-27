dna = "ATGCGATATCGCG"
a,t,g,c = dna.count('A'), dna.count('T'), dna.count('G'), dna.count('C')
print(f"A:{a} T:{t} G:{g} C:{c}")
print(f"Total: {len(dna)} | GC% = {(g+c)/len(dna)*100:.2f}%")
