dna = "ATGCGATATCGCG"
comp = dna.translate(str.maketrans("ATGC","TACG"))
rev_comp = comp[::-1]
print(f"DNA: {dna}")
print(f"Reverse Complement: {rev_comp}")
