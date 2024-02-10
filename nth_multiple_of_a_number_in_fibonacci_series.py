def fibonacci_multiple(n, multiple):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    multiple_count = 0
    index = 0

    while multiple_count < n:
        current_number = fib_sequence[index]
        if current_number % multiple == 0:
            multiple_count += 1
        index += 1

    return fib_sequence[index - 1]

# Example usage:
n = int(input("Enter the value of n: "))
multiple = int(input("Enter the multiple: "))

result = fibonacci_multiple(n, multiple)
print(f"The {n}th multiple of {multiple} in the Fibonacci series is: {result}")