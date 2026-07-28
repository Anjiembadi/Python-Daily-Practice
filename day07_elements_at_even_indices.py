#Print Elements at Even Indices of a List
numbers = input("Enter the list elements separated by spaces: ").split()

print("Elements at even indices are:", end=" ")

for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i], end=" ")