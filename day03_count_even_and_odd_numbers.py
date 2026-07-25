def count_even_odd(numbers):
    even = 0
    odd = 0

    for num in numbers:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
even, odd = count_even_odd(numbers)

print("Even:", even)
<<<<<<< HEAD
print("Odd:", odd)
=======
print("Odd:", odd)
>>>>>>> 4b6b000 (Day 4: Square From 1 to N)
