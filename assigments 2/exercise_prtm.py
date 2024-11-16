# Dictionary that maps each amino acid to its monoisotopic mass
monoisotopic_masses = {
    'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259, 'F': 147.06841,
    'G': 57.02146, 'H': 137.05891, 'I': 113.08406, 'K': 128.09496, 'L': 113.08406,
    'M': 131.04049, 'N': 114.04293, 'O': 237.15815, 'P': 97.05276, 'Q': 128.05858,
    'R': 156.10111, 'S': 87.03203, 'T': 101.04768, 'V': 99.06841, 'W': 186.07931,
    'Y': 163.06333
}

# Function to calculate the total weight of a protein based on its amino acid sequence
def calculate_protein_weight(protein_string):
    tot_weight = 0
    
    # Iterate through each amino acid in the protein string
    for amino_acid in protein_string:
        tot_weight += monoisotopic_masses[amino_acid]        # # Add the monoisotopic mass of the amino acid to the total weight
    
    return tot_weight

#input
protein = "SKADYEK"
print(round(calculate_protein_weight(protein), 3))
