
def countdown(s,i):
    if i<=0:
        print("INVALID PARAMETERS!")
    while s>=0 and i>0:
        print(s)
        s-=i 

# sum multiples

def sum_multiples(x):
    count=0
    total=0
    i=1
    while i<=x:
        if i%3==0 or i%7==0 : #check if i is div by 3 or 7 
            count+=1 #one more number
            total+=i #sum of numbers
            i+=1
        elif i==x:
            return
        else:i+=1
    print("count=", count,"and total=", total, sep=" ")

#project euler1 
def threeorfive(q):
    toftotal=0
    i=1
    while i<q:
        if i%3==0 or i%5==0:
            toftotal+=i 
            i+=1
        elif i%15==0:
            toftotal-=i
        else: i+=1
    print(toftotal)

def collatz_chain_skips(x):
    sum=0
    if x==1:
        sum+=1
        print(sum)
    while x>1:
        if x%2==0: 
            x//=2
        else:
            sum+=x
            print(x, end=" ")
            x=3*x+1
        if x==1:
            sum+=1
            print(x,sum, sep="")
            return sum
    if x<=0:
        print("Invalid Input")
        return -1

def sum_list(list):
    sum=0
    if list ==[]:
        print("list must have a value")
        return 0
    else:
        for i in range(len(list)):
            sum+=list[i]
    print(sum)
    return sum
            
def separator(sep,list):
    if len(list)==0:
        print("Nothing to do here...")
        return
    for i in range(len(list)):
        print(list[i],end="")
        if i+1<len(list):
            print(sep,end="")
    print()

def listHaircut(list):
    if len(list)==0:
        print("List cannot be empty")
    if len(list)<=2:
        print('[]')
        return []
    trimmed_list=[]
    for i in range(1,len(list)-1):
        trimmed_list+=[list[i]]
    print(trimmed_list)

def listTest(A,B):
    if len(A) <= len(B):
        return -1
    for i in range(len(B)):
        B[i] = B[i] / A[i + 1]
        print(B[i])
    return A[0]

def backwardsList(L):
    for i in range(len(L)-1,-1,-1):
        print(L[i], end=" ")
    print()

def listSum(L):
    summed_list=[]
    sum=0
    for i in range(len(L)):
        sum+=L[i]
        summed_list+=[sum]
    print(summed_list)

def reverseInputList(L):
    reversed_list=[]
    for i in range(len(L)-1,-1,-1):
        reversed_list+=[L[i]]
    print(reversed_list)

def windowedAverage(L,i): #win size=3
    window_avg_list=[]
    if len(L)<3:
        print('Cannot take a windowed average')
    if i>=len(L)-2:
        print('Window outside of list!!!!! Gah!')
        return 0
    while i<len(L)-2:
        avg_of_3=((L[i]+L[i+1]+L[i+2])/3)
        window_avg_list+=[avg_of_3]
        i+=1
    print(window_avg_list)

def merge_lists(a,b):
    mergedList=[]
    aIndex=0
    bIndex=0
    while aIndex+bIndex<len(a)+len(b):
        if bIndex==len(b) or (aIndex<len(a) and a[aIndex]<b[bIndex]):
            mergedList+=[a[aIndex]]
            aIndex+=1
        else:
            mergedList+=[b[bIndex]]
            bIndex+=1
    print(mergedList)

def in_list(list,target):
    for i in range(len(list)):
        if list[i]==target:
            return True
    return False

def filter_list(l1,l2): #check if an element in l2 is matching with l1, if not add to outl, if so pass
    outl=[]
    for i in range(len(l2)):
        filt=0
        for j in range(len(l1)):
            if l2[i]==l1[j]:
                filt=1
        if filt==0:
            outl+=[l2[i]]

    print(outl)

def age_check(n,a):
    outl=[]
    if len(n)!=len(a):
        print("All names must be associated with an age!")
        return 0
    else: 
        for i in range(len(n)):
            if a[i]>=18:
                outl+=[n[i]]
            else: pass
    print(outl)

def rc_sum(l):
    retl=[[],[]]
    for i in range(len(l)):
        sum=0
        for j in range(len(l[i])):
            sum+=l[i][j]
        retl[0]+=[sum]
    for j in range(len(l[i])):
        sum=0
        for i in range(len(l)):
            sum+=l[i][j]
        retl[1]+=[sum]

    print(retl)


def band_aid(l):
    allcombos=[]
    # for i in range(len(l)):
    #     llen=len(l[0])
    #     if len(l[i])!=llen:
    #         print("All roles must have the same number of members!")
    '''dont really need this part'''
    
    ## i: row list of people in a given role; j: number of categories 
    for i in range(len(l[0])):
        for j in range(len(l[1])):
            for k in range(len(l[2])):
                combo=[]
                combo+=[l[0][i],l[1][j],l[2][k]]
                allcombos+=[combo]
    print(allcombos)

def find_peaks(l):
    peaks=[]
    for i in range(len(l)):
        if len(l[i])==len(l):
            print("Argument must be a square matrix!")
            return 
        
    for i in range(l):
        for j in range(l[i]):
            if i==0:
                if l[i][j]<l[i][j+1] or l[i][j]<l[i+1][j]:
                    pass
                else: peaks+=[[i,j]]
    pass; '''finish later'''

def rotate(l): #l is a matrix 
    newmat=l
    for i in range(len(l)):
        for j in range(len(l[i])):
            l[i][j]=newmat[j][i]
    print(newmat)
    '''very close, just need to fix bottom row '''
        
def type_name(x) -> str:
    if isinstance(x,bool):
        print("Bool")
    elif isinstance(x,str):
        print("String")
    elif isinstance(x,int):
        print("Int")
    elif isinstance(x,float):
        print("Float")
    else:
       dim=1
       x=x
       while dim>=1:
           if x==[]:
               print(dim,"D List")
           elif isinstance(x[0],list):
               dim+=1
               x=x[0]


def get_table(x,y):
    outl=[]
    for i in range(x,y+1):
        suboutl=[]
        for j in range(x,y+1):
            suboutl+=[i*j]
        outl+=[suboutl]
    print(outl)


def main():
    get_table(1,12)


if __name__=="__main__":
    main()

