n=int(input("Enter the number:"))
if n<=1:
          print("Not prime number")
else:
        if n>=2:
          for i in range(2,n):
                        if n%i==0:
                                print("Not prime Number")
                                break
          else:
                  print('Prime Number')
                        