from Bio.Seq import Seq

rna_seq = Seq("AUGGCCAUUGUAA")
protein = rna_seq.translate()

print(f"RNA: {rna_seq}")
print(f"Protein: {protein}")
