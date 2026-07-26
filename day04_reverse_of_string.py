#write a function to reverse a string
def reverse_string(n):
          rev=""
          for ch in n:
                  rev=ch+rev
          return rev
s=input()
print(reverse_string(s))