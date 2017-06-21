seq1 = 'thequickbro'
seq2 = 'dog'


def longest_common_substring(seq1, seq2):
    """attempts to find the longest common substring between two strings"""
    match = ''
    longest = ''
    for i in range(0, len(seq2)+1):
        for j in range(0, len(seq2)+1):
            if seq2[i:j] in seq1:
                match = (seq2[i:j])
                if len(match) > len(longest):
                    longest = match
    print(longest)


longest_common_substring(seq1, seq2)
