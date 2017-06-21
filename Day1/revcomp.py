def reverse_complement(seq, material='DNA'):
    """computes the reverse complement of a sequence."""
    # deleting DNA makes material a required arguement
    rev_seq = ''

    for base in reversed(seq):
        rev_seq += complement_base(base, material=material)
    return rev_seq


def complement_base(base, material='DNA'):
    """Returns a watson-crick complement of a base"""
    base = base.lower()
    if base in 'a':
        if material == 'DNA':
            return 'T'
        elif material == 'RNA':
            return 'U'
    elif base in 'tu':
        return 'A'
    elif base in 'g':
        return 'C'
    else:
        return 'G'


reverse_complement('AGCTCGTGCTGCTGCTCTGC', material='RNA')
reverse_complement('AGCTCGTGCTGCTGCTCTGC', material='DNA')
