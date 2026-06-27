from Bio import SeqIO

# Fasta file read karo
for record in SeqIO.parse("example.fasta", "fasta"):
    print(f"Name: {record.id}")
    print(f"Sequence: {record.seq}")
    print(f"Length: {len(record.seq)} bp")
    print(f"GC%: {round(100 * (record.seq.count('G') + record.seq.count('C')) / len(record.seq), 2)}")
