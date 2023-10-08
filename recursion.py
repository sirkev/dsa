def find_factorial(n):
    if n==1: 
        return 1
    else:
        return n * find_factorial(n-1)



print(find_factorial(int(input("Enter a number to find its factorial:"))))
