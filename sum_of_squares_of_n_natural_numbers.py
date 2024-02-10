def sum_of_squares(n):
    # Initialize the sum variable to store the result
    sum_result = 0
    
    # Loop through the first n natural numbers and add their squares to the sum
    for i in range(1, n + 1):
        sum_result += i ** 2
    
    # Return the final sum
    return sum_result

# Example: Find the sum of squares of the first 5 natural numbers
n = int(input("Enter the number : "))
result = sum_of_squares(n)

# Display the result
print(f"The sum of squares of the first {n} natural numbers is: {result}")