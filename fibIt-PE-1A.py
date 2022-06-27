#Sarah Viall
#Fibonacci Iterative

def fib(n):

    if N==0 or N==1: #base cases
        return N
    else:
        Fa=0
        Fb=1
        i=0
        while i<N-1:
            Fc=Fa+Fb
            #print(Fc) #debug
            Fa=Fb
            Fb=Fc
            i+=1
        return Fc


N=int (input("Enter requested Nth term: "))
print(fib(N))