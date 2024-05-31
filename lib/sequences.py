#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        # If the length is less than or equal to 0, print an empty list
        print([])
        return

    fibonacci_sequence = []

    # Handle the first two numbers separately
    if length >= 1:
        fibonacci_sequence.append(0)
    if length >= 2:
        fibonacci_sequence.append(1)

    # Generate the remaining Fibonacci numbers
    while len(fibonacci_sequence) < length:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    print(fibonacci_sequence)

#testing function
print_fibonacci(9)