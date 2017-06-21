import os

with open('data/salmonella_spi1_region.fna', 'r') as f:
    for i, line in enumerate(f):
        if i > 0:
            dna_string = line.rstrip()


def gc_blocks(seq, block_size):
    seq = seq.upper()
    gc_con = []
    for i in range(0, len(seq) // block_size * block_size, block_size):
        g_con = seq[i: i + block_size].count('G')
        c_con = seq[i: i + block_size].count('C')
        print(g_con)
        print(c_con)
        gc_con.append((g_con + c_con) / block_size)
    return gc_con

gc_blocks('ATGACTACGT', 4)

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
gc_map(dna_string, 1000, 0.45)
