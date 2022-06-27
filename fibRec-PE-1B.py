#Sarah Viall
#Fibonacci Recursion


def fibR(n):

    if n<=1: #0 and 1 are base cases
        return n
    else:
        return(fibR(n-1)+fibR(n-2))




N=int (input("Enter requested Nth term: "))
print(fibR(N))