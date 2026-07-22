# Write a function to return the sum of all natural numbers up to n using a for loop.
def sum_natural(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter a number: "))
print("Sum:", sum_natural(n))