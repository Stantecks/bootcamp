import bioinfo_dicts as bd


def one_to_three(seq):
    """
    Converts a protein sequence using one-letter abbreviations
    to one using three-letter abbreviations
    """
    # Convert seq to upper
    seq = seq.upper()

    # Do conversion, checking each input is AA valid.
    aa_list = []
    for amino_acid in seq:
        if amino_acid not in bd.aa.keys():
            raise RuntimeError(amino_acid + ' is not a valid amino acid.')
        aa_list += [bd.aa[amino_acid], '-']

    # Return results
    return ''.join(aa_list[:-1])
