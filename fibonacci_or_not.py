def is_perfect_square(num):
    sqrt_num = int(num**0.5)
    return sqrt_num**2 == num

def is_fibonacci(number):
    # A number is Fibonacci if and only if one of (5 * n^2 + 4) or (5 * n^2 - 4) is a perfect square
    check1 = 5 * number**2 + 4
    check2 = 5 * number**2 - 4

    return is_perfect_square(check1) or is_perfect_square(check2)

# Example Usage
user_input = int(input("Enter a number to check if it's a Fibonacci number: "))
if is_fibonacci(user_input):
    print(f"{user_input} is a Fibonacci number.")
else:
    print(f"{user_input} is not a Fibonacci number.")