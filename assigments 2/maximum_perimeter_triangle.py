def maximumPerimeterTriangle(sticks):
    sticks.sort()                          # Sort the lengths of the sticks

    # Iterate over the list sorted in order to find the triangle with the largest perimeter
    for i in range(len(sticks) - 1, 1, -1):
        a, b, c = sticks[i - 2], sticks[i - 1], sticks[i]
        if a + b > c:                                        # if it satisfies the triangle inequality...
            return [a, b, c]                                 #....returns the sides of the triangle in ascending order
    
    return [-1]                                              #if there are no good trigles return -1

# Sample Input 0
sticks = [1, 1, 1, 3, 3]
result = maximumPerimeterTriangle(sticks)
print(result)
