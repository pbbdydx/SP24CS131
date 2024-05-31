
## CS131 Assignment 11
## Prajwal Bhandari
## March 2024


def collatz_chain(x:int) -> int:
    if x < 1 or not isinstance(x,int):
        print("Invalid Input")
        return -1
    if x == 1: 
        print(1) 
        return 1
    
    if x%2==0:
        print(int(x), end=" ")
        return x + collatz_chain(x//2)  
    else:
        print(int(x), end=" ")
        return x + collatz_chain(int(3*x+1))
    

def collatz_depth(x:int) ->int :
    return cd_helper(x,0) 

def cd_helper(x,skips) ->int:
    if x < 1 or not isinstance(x,int):
        print("Invalid Input")
        return -1
    if x == 1: 
        print(1) 
        print("Skipped",skips,"numbers. ")
        return 1
    
    if x%2==0:
        skips+=1
        return x + cd_helper(x//2,skips)  
    else:
        print(int(x), end=" ")
        return x + cd_helper(int(3*x+1),skips)
   
    
def binary_search(l:list,target:int) ->int :
    mid=len(l)//2
    if len(l)==0:
        return -1
    
    if len(l)==1:
        if l[0]==target: 
            return 0
        else: 
            return -1

    if l[mid]==target: 
        return mid
    
    if target > l[mid]:
        for i in range(0,mid+1):
            l.pop(0)
        value=binary_search(l,target)
        if value==-1:
            return value
        return mid + value +1
    else:
        for i in range(len(l),mid,-1):
            l.pop()
        return binary_search(l,target) 

    
def merge_sort(l:list) ->list :
    ll=[]
    rl=[]
    if len(l)<=1:
        return l
    
    mid=len(l)//2
    for i in range(len(l)):
        if i<mid:
            ll.append(l[i])
        else:
            rl.append(l[i])
    
    return merge(merge_sort(ll), merge_sort(rl))


def merge(a,b):
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
    return ml


def main():
    print(collatz_chain(3))
    pass 

if __name__== "__main__":
    main()
    





