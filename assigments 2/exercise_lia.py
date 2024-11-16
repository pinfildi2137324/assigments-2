
def factorial(n):
    #calculate the factorial of n
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def binomial_coefficient(n, x):
    #calculate the binomial coefficient
    if x > n:
        return 0
    return factorial(n) // (factorial(x) * factorial(n - x))

def probability(k, N):
    #calculate the probability that at least N organisms Aa Bb are in the k-th generation.
    n = 2 ** k
    p_AaBb = 1 / 4
    prob_less_than_N = 0
    for x in range(N):
        prob_x_AaBb = binomial_coefficient(n, x) * (p_AaBb ** x) * ((1 - p_AaBb) ** (n - x))
        prob_less_than_N += prob_x_AaBb

    prob_at_least_N = 1 - prob_less_than_N
    
    return prob_at_least_N

#input
k = 2
N = 1
print(round(probability(k, N), 3))  
