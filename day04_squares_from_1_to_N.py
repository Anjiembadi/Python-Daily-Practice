#Squares of Numbers (1 to N)
def print_squares(n):
  for i in range(1,n+1):
    print(f"square of {i} is:",i*i)
n=int(input("Enter the number:"))
print_squares(n)