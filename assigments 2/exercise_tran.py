
def transition_transversion_ratio(s1, s2):
    transitions = 0
    transversions = 0
    
    # Define transition pairs
    transitions_pairs = [('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')]
    
    # Loop over the corresponding characters of the two strings
    for base1, base2 in zip(s1, s2):
        if base1 != base2:                 # consider only mismatches
            if (base1, base2) in transitions_pairs or (base2, base1) in transitions_pairs:
                transitions += 1  
            else:
                transversions += 1  
    
    # Return the ratio, handling the case where there are no transversions
    if transversions == 0:
        return float('inf')                       # If there are no transversions, return infinity (or a large number)
    else:
        return transitions / transversions

# Parse the FASTA input to extract sequences
def parse_fasta(fasta_str):
    sequences = []
    current_sequence = []
    
    for line in fasta_str.splitlines():
        line = line.strip()
        if line.startswith(">"):                                # Ignore headers
            if current_sequence:
                sequences.append("".join(current_sequence))
                current_sequence = []
        else:
            current_sequence.append(line)
    
    if current_sequence:                                       # Append the last sequence
        sequences.append("".join(current_sequence))
    
    return sequences

# input
fasta_input = """>Rosalind_0209
GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGA
AGTACGGGCATCAACCCAGTT
>Rosalind_2200
TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGC
GGTACGAGTGTTCCTTTGGGT
"""


sequences = parse_fasta(fasta_input)

s1 = sequences[0]
s2 = sequences[1]

result = transition_transversion_ratio(s1, s2)
print(f"{result:.11f}")
