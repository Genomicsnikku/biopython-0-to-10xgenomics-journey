from Bio.SeqUtils import GC_skew

dna = "ATGCGATATCGCGATGCGATATCGCG"
window_size = 10

for i in range(0, len(dna) - window_size, window_size):
    window = dna[i:i+window_size]
    skew = GC_skew(window)
    print(f"Window {i}-{i+window_size}: {skew:.3f}")
