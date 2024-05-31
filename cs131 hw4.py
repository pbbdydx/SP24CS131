
## CS131 Assignment 4
## Prajwal Bhandari
## Feb 2024

def copy_list(L):
    copiedList=[]
    for i in range(len(L)):
        copiedList+=[L[i]]
    return copiedList
    

def reverse_list(L):
    reversedList=[]
    for i in range(len(L)-1,-1,-1):
        reversedList+=[L[i]]
    return reversedList

def modify_list(x,L):
    outList=[]
    for i in range(len(L)):
        outList+=[x+L[i]]
    return outList

def combine_lists(A,B):
    combinedList=[]
    if len(A)<=len(B):
        for i in range(len(A)):
            combinedList+=[A[i]+B[i]]
    elif len(A)>len(B):
        for i in range(len(B)):
            combinedList+=[A[i]+B[i]]
    return combinedList

def blackjack(L):
    total=0
    for i in range(len(L)):
        if L[i]>11 or L[i]<1:
            print("Cheating!")
            return
        else: total+=L[i]
    if total==21:
            print("Total: ", total," .", sep="")
            return #blah blah blah 
    if total>21:
        tempTotal=0
        for k in range(0,len(L)):
            if tempTotal+L[k]>21:
                print("Total: ", total, " is a bust. Card  ",k+1," caused the bust.", sep="")
                return
            tempTotal+=L[k]
    if total<21:
        print("Total: ", total," .", sep="")
        return
    
def sum_indices(F,G):
    sum=0
    if len(F)==0 or len(G)==0:
        print("Nothing to sum here.")
        return 0.0
# want to check for any bad inceces before we even sum.
    for i in range(len(F)):
        if F[i]>len(G)-1 or F[i]<0:
            print("Out of bounds index. Check one-index ",i+1," in the direction list.", sep="")
            return 0.0
    for i in range(len(F)):
        sum+=G[F[i]]
    print("Your total is ",sum,".", sep="")
    return sum

def merge_lists(a,b):
    ml=[]
    i=0
    j=0
    while i+j<len(a)+len(b):
        if j==len(b) or (i<len(a) and a[i]<b[j]):
            ml+=[a[i]]
            i+=1
        else:
            ml+=[b[j]]
            j+=1
    print(ml)
    return ml

def windowed_average(n,L):
    if n==0: 
        return L
    if n>(len(L)-1)//2:
        print("Window too big!")
        return
    elif n<0:
        print("Window size doesnt mean anything. Try again!")
        return 
    aonList=[]
    for i in range(n,len(L)-n):
        sum=0
        for k in range(n+1):
            if k==0:
                sum+=L[i]
            else:
                sum+=L[i+k]
                sum+=L[i-k]
        aon=(sum)/(2*n+1)
        aonList+=[aon]
    print(aonList)
    return aonList

def main():
    pass

if __name__ == "__main__":
    main()