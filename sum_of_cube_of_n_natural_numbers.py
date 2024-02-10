def sum_of_cubes(n):
    if n <= 0:
        return "Please enter a positive integer."
    
    # Using the formula for the sum of cubes: (1^3 + 2^3 + 3^3 + ... + n^3) = ((n * (n + 1)) / 2)^2
    result = ((n * (n + 1)) // 2) ** 2
    return result

# Get user input
n = int(input("Enter a positive integer (n): "))

# Calculate and print the sum of cubes
result = sum_of_cubes(n)
print(f"The sum of cubes of the first {n} natural numbers is: {result}")