
## CS131 Assignment 3
## Prajwal Bhandari
## Jan 2024


#Collatz Problem: 
def collatz_chain(x):
    sum=0
    if x<=0:
        print("Invalid Input")
        return -1
    if x==1:
        sum+=1
        print(sum)
        return sum
    print(x, end=" ")
    while x>1:
        if x%2==0: 
            sum+=x
            x//=2
            print(x, end=" ")
        else:
            sum+=x
            x=3*x+1
            print(x, end=" ")
        if x==1:
            sum+=1
            print("")
            return sum
def collatz_chain_skips(x):
    sum=0
    if x==1:
        sum+=1
        print(sum)
        return sum
    while x>1:
        if x%2==0: 
            x//=2
        else:
            sum+=x
            print(x, end=" ")
            x=3*x+1
        if x==1:
            sum+=1
            print(x)
            return sum
    if x<=0:
        print("Invalid Input")
        return -1

#prime function
def is_prime(p):
    if p<2: return False

    for i in range(2,int(p**1/2+1)):
        if p%i==0: return False
    return True

def population_sim(initialPopulation, rateofChange, CarryingCap):
    starting_conditions=1 
    if initialPopulation<0 or initialPopulation%1.0!=0:
        starting_conditions=0
        print("Starting population must be a positive whole number.")
    if rateofChange<0 or rateofChange> 1:
        starting_conditions=0
        print("Rate of change must be between 0.0 and 1.0, inclusive!")
    if CarryingCap<0 or CarryingCap%1.0!=0:
        starting_conditions=0
        print("Carrying capacity must be a positive whole number.")
    if starting_conditions==0:
        return -1
    if initialPopulation>=CarryingCap:
        return initialPopulation-(initialPopulation%1.0)

    if starting_conditions==1:
        popChange=rateofChange*initialPopulation*(1-(initialPopulation/CarryingCap))
        percentChange= ((initialPopulation+popChange)/initialPopulation)
        i=1
        newpop=initialPopulation+popChange
        while percentChange>=1.01:
            newpop=initialPopulation+popChange
            if newpop%1.0>=0.5:
                newpop_rounded=(newpop-newpop%1.0)+1
            else:newpop_rounded=newpop-newpop%1.0
            if initialPopulation%1.0>=0.5:
                initialPopulation_rounded=(initialPopulation-initialPopulation%1.0)+1
            else: initialPopulation_rounded=initialPopulation-initialPopulation%1.0
            print(i, ":", initialPopulation_rounded, "->", newpop_rounded)
            i+=1
            initialPopulation=newpop
            popChange=rateofChange*initialPopulation*(1-(initialPopulation/CarryingCap))
            percentChange=((initialPopulation+popChange)/initialPopulation)
        popChange=rateofChange*initialPopulation*(1-(initialPopulation/CarryingCap))
        percentChange= ((initialPopulation+popChange)/initialPopulation)
        newpop=initialPopulation+popChange
        if newpop%1.0>=0.5:
            newpop_rounded=(newpop-newpop%1.0)+1
        else:newpop_rounded=newpop-newpop%1.0
        if initialPopulation%1.0>=0.5:
            initialPopulation_rounded=(initialPopulation-initialPopulation%1.0)+1
        else: initialPopulation_rounded=initialPopulation-initialPopulation%1.0
        print(i, ":", initialPopulation_rounded, "->", newpop_rounded)
        return initialPopulation


def main():
    pass
    
if __name__ == "__main__":
    main()
