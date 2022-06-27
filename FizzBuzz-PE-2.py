#Sarah Viall
#FizzBuzz


print("Let's play FizzBuzz!")
N=int (input("How high would you like to count? "))

i=1
while i<=N:
    if i%15==0:
        print("FizzBuzz", end='') #  end=''  no new line
    elif i%5==0:
        print("Buzz",end='')
    elif i%3==0:
        print("Fizz",end='')
    else:
        print(i,end='')
    i+=1
    if i<=N:
        print(", ", end='') ## commas between each exepct for last
    
    
    


##Research Links
## https://en.wikipedia.org/wiki/Fizz_buzz