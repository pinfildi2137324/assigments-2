# Parsing the FASTA input into sequences
def parse_fasta(fasta_input):
    lines = fasta_input.strip().split("\n")         # Split input into lines
    sequences = []
   
    current_sequence = ""  
    for line in lines:
        if line.startswith(">"):                   # Check for sequence header
            if current_sequence:                   # If we have accumulated a sequence, save it
                sequences.append(current_sequence)
            current_sequence = ""  
        else:
            current_sequence += line.strip()       # Add sequence line to the current sequence

    if current_sequence: 
        sequences.append(current_sequence)
       
    return sequences


# Function to transcribe DNA to RNA 
def transcribe_to_rna(dna):
    return dna.replace('T', 'U')      # Replace all T with uracil U


# Function to translate RNA to protein using a codon table
def translate_rna_to_protein(rna):
    codon_table = {
        'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': '', 'UAG': '',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'UGU': 'C', 'UGC': 'C', 'UGA': '', 'UGG': 'W',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
   
    protein = []  
    # Iterate through the RNA sequence in codons 
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]                           # Extract the codon (3 bases)
        if codon in codon_table:                     # Check if codon exists in the table
            amino_acid = codon_table[codon]          # Get the corresponding amino acid
            if amino_acid:                           # Ignore stop codons
                protein.append(amino_acid)           # Add the amino acid to the protein list
    return ''.join(protein)                          # Join the list into a single string and return


# Function to remove introns from DNA
def remove_introns(dna, introns):
    for intron in introns:                           # Loop through all introns and remove them
        dna = dna.replace(intron, '')  
    return dna


# Main function to process the entire sequence from FASTA input
def main(fasta_input):
    sequences = parse_fasta(fasta_input)                          # Parse the input into sequences
    dna_sequence = sequences[0]                                   # The first sequence is the full DNA sequence
    introns = sequences[1:]                                       # All subsequent sequences are considered introns
    exons_dna = remove_introns(dna_sequence, introns)             # Remove introns from the DNA sequence
    rna_sequence = transcribe_to_rna(exons_dna)                   # Transcribe the exons to RNA
    protein_sequence = translate_rna_to_protein(rna_sequence)     # Translate RNA to protein
    return protein_sequence


#FASTA input
fasta_input = """>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
"""


protein = main(fasta_input)
print(protein)
