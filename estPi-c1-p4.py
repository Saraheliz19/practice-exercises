#Sarah Viall  Chapter 1: Project 4
#Estimating Pi


i=int (input("Enter number of iterations: "))

print (i)
num=4
piold=0
posneg=1
for d in range (1,i*2,2):
    pi=num/d*posneg
    pisum=piold+pi
    piold=pisum
    posneg=posneg*-1
print(pisum)