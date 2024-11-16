
def parse_fasta(fasta_data):
    # Parse the FASTA format into a list of DNA strings
    strings = []
    current_dna = []
    
    for line in fasta_data.strip().splitlines():
        line = line.strip()
        if line.startswith(">"):                        # Skip header lines
            if current_dna:                             # Add the previous DNA string if it exists
                strings.append("".join(current_dna))
                current_dna = []
        else:
            current_dna.append(line)                        # Concatenate sequence lines
    
    if current_dna:                                     # Add the last DNA string
        strings.append("".join(current_dna))
    
    return strings

def create_profile_matrix(strings):
    lenght = len(strings[0])
    profile={nucleotide: [0] * lenght for nucleotide in "ACGT"}

    for seq in strings:
        for index, nucleotide in enumerate(seq):
            profile[nucleotide][index] +=1
    return profile

def create_consensus_string(profile):
    consensus=[]
    for i in range(len(next(iter(profile.values())))):
        max_nucleotide = max(profile, key=lambda x: profile[x][i])
        consensus.append(max_nucleotide)
    return ''.join(consensus)


if __name__ == "__main__":
    fasta_data= """>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT
"""

    strings= parse_fasta(fasta_data)
    profile_matrix= create_profile_matrix(strings)
    consensus_string=create_consensus_string(profile_matrix)
    print(consensus_string)
    for nucleotide in "ACGT":
        print(f"{nucleotide}: {' '.join(map(str, profile_matrix[nucleotide]))}")