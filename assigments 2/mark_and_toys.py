def maximumToys(prices, k):
    prices.sort()             #sort the prices
    total_budget = 0
    toy_number = 0

    #iterate over the prices
    for price in prices:
        # Check if the current price can be added without exceeding the budget
        if total_budget + price <= k:
            total_budget += price  #add the price to the total budget
            toy_number += 1         #increases the number of toys
        else:
            break 

    return toy_number

# Sample Input 0
prices = [1, 12, 5, 111, 200, 1000, 10]
k = 50
result = maximumToys(prices, k)
print(result)
