import os


def gc_map(seq, block_size, gc_thresh):
    seq = seq.lower()
    dnastr = ''
    for i in range(0, len(seq) // block_size * block_size, block_size):
        g_con = seq[i: i + block_size].count('g')
        c_con = seq[i: i + block_size].count('c')
        if (g_con + c_con) / block_size > gc_thresh:
            dnastr += seq[i: i+block_size].upper()
        else:
            dnastr += seq[i: i+block_size].lower()
    return dnastr


def sixty_chunks(seq):
    dna_data = []
    for i in range(0, len(seq), 60):
        dna_data.append(seq[i:i+60])
    return dna_data


dna_string = ''

with open('data/salmonella_spi1_region.fna', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            dna_string += line.rstrip()

dna_string = gc_map(dna_string, 1000, 0.45)
dna_list = sixty_chunks(dna_string)


with open('data/salmonella_spi1_region.fna', 'r') as f, open('data/exer2_3.fna', 'w') as f_out:
    f_list = f.readlines()
    print(f_list[0].rstrip(), *dna_list, file=f_out, sep='\n')
