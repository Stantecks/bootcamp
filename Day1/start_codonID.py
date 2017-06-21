start_codon = 'ATG'
seq = 'AGTGCGCAGCATCGCAGCATCACGACTGCATCGACTAGCTAGCAGTGCGACGTCAG'

# Initialize the sequene index
i = 0

# Scan for start codon
while seq[i:i+3] != start_codon and i < len(seq):
    i += 1

if i == len(seq):
    print('start codon not found')
else:
    print('start codon at index', i)
