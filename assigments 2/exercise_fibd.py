 
def rabbit_population(n,m):
    # Base case: If the number of months (n) is 1, there is only 1 rabbit pair
    if n == 1: 
        return 1
    
    rabbits_by_age = [0] * m 

    rabbits_by_age[0] = 1

    # For each month (starting from month 2), simulate rabbit reproduction
    for i in range(2, n + 1):                                 # Loop through months from 2 to n                           
        new_born_rabbits = sum(rabbits_by_age[1:])            # It is the sum of all rabbits that are between 1 and m-1 months old
        
        # Shift the rabbit counts by age 
        for j in range(m-1, 0, -1):
            rabbits_by_age[j] = rabbits_by_age[j - 1]

        rabbits_by_age[0]= new_born_rabbits

    tot_pairs = sum(rabbits_by_age)
    return tot_pairs

n = 6
m = 3
print(rabbit_population(n,m))

