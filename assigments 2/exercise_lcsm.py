# Parsing a FASTA string into a list of DNA sequences:
def parse_fasta(fasta_data):
    dna_sequences = []  
    current_sequence = []  

    # Loop through each line in the FASTA string
    for line in fasta_data.splitlines():
        line = line.strip()                           # Remove leading/trailing whitespaces
        if line.startswith(">"):                      # Check if the line is a header
            # If there is a current sequence, append it to the list of sequences
            if current_sequence:
                dna_sequences.append("".join(current_sequence))
                current_sequence = []                 
        else:
            current_sequence.append(line)             # Add DNA sequence data to current sequence
        
    # Append the last sequence if there's any remaining data
    if current_sequence:
        dna_sequences.append("".join(current_sequence))
    
    return dna_sequences  

# Checking if a substring is present in all strings:
def contains_substring(sub, strings):
    return all(sub in s for s in strings)               # Return True if the substring is found in all the strings in the list

# Finding the longest common substring:
def find_longest_common_substring(strings):
    # Find the shortest string in the list to reduce search space
    shortest_string = min(strings, key = len)
    left, right = 1, len(shortest_string)               # Set initial search range for substring length
    longest_substr = ""  

    # Use binary search to find the longest common substring
    while left <= right:
        mid = (left + right) // 2  
        found = False                                   # Flag to check if a valid substring is found

        # Check all substrings of length 'mid' in the shortest string
        for start in range(len(shortest_string) - mid + 1):
            substr = shortest_string[start:start + mid]
            if contains_substring(substr, strings):      # Check if this substring is in all strings
                longest_substr = substr  
                found = True                             # A valid substring has been found
                break

    
        if found:
            left = mid + 1                       # Try to find a longer substring
        else:
            right = mid - 1                      # Try to find a shorter substring

    return longest_substr 

# Input
fasta_input = """>Rosalind_1
GATTACA
>Rosalind_2
TAGACCA
>Rosalind_3
ATACA
"""

dna_sequences = parse_fasta(fasta_input)

longest_common = find_longest_common_substring(dna_sequences)
print(longest_common)

