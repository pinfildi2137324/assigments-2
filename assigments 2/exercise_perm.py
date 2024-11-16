def generate_permutations_recursive(nums_list, index, permutations):
    if index == len(nums_list):
        permutations.append(nums_list[:])                          # Append a copy of the current permutation
    else:
        for i in range(index, len(nums_list)):
            # Swap the current index with the loop index
            nums_list[index], nums_list[i] = nums_list[i], nums_list[index]
            # Recursively generate permutations for the next part of the list
            generate_permutations_recursive(nums_list, index + 1, permutations)
            # swap back
            nums_list[index], nums_list[i] = nums_list[i], nums_list[index]

def generate_permutations(n):
    # List of numbers from 1 to n
    nums_list = list(range(1, n + 1))
    permutations = []  
    
    generate_permutations_recursive(nums_list, 0, permutations)
    
    print(len(permutations))
    
    for perm in permutations:
        print(" ".join(map(str, perm)))

#Input
n = 3

generate_permutations(n)

