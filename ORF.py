def longest_orf(seq):
    start_codon = 'ATG'
    stop_codon = ('TGA', 'TAG', 'TAA')
    pot_starts = []
    frame_coord = []
    long_orf = 0
    seq = seq.upper()
    for i in range(0, len(seq)):
        if seq[i:i+3] in start_codon:
            pot_starts.append(i)
    for j in pot_starts:
        for k in range(j, len(seq), 3):
            if seq[k:k+3] in stop_codon:
                if abs(j - k) > long_orf:
                    long_orf = abs(j - k)
                    frame_coord = [j, k+3]
    return seq[frame_coord[0]:frame_coord[1]]


dna_string = ''

with open('data/salmonella_spi1_region.fna', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            dna_string += line.rstrip()

longest_orf(dna_string)
