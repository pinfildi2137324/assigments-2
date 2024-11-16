def reverse_complement(dna):
    # reverse complement of the DNA string
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna):
    #Finds reverse palindromes of length between 4 and 12 in the DNA string
    n = len(dna)
    reverse_palindromes = []
    
    # Check all substrings of length 4 to 12
    for length in range(4, 13):
        for i in range(n - length + 1):
            substring = dna[i:i+length]
            if substring == reverse_complement(substring):
                reverse_palindromes.append((i + 1, length))  
    
    return reverse_palindromes

#FASTA Input
fasta_input = """>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
"""

# Function to parse FASTA formatted string into sequences
def parse_fasta(fasta_str):
    sequences = []
    current_sequence = []
    for line in fasta_str.splitlines():
        line = line.strip()
        if line.startswith(">"):  
            if current_sequence:
                sequences.append("".join(current_sequence))    # Join the sequence and append to the list
                current_sequence = []                          # Reset for the next sequence
        else:
            current_sequence.append(line) 
    if current_sequence:
        sequences.append("".join(current_sequence))
    return sequences

# Parse the input FASTA string
sequences = parse_fasta(fasta_input)

# Find reverse palindromes in each DNA sequence
for seq in sequences:
    result = find_reverse_palindromes(seq)    
    for position, length in result:
        print(position, length)
