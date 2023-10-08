def pyramid(n):
    stars = 1
    while stars <=n:
        spaces = int((n-stars)/2)
        print(" " * spaces + "*" * stars + " "* spaces)
        stars +=2
    
pyramid(int(input('Enter Number of stars to print then press enter:')))

