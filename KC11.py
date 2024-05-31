
def factorial(n):
    if n==0 or n==1:
        return 1
    if n>1:
        return n*factorial(n-1)
    if n<0:
        return -1*(factorial(-n))

def countdown_loop(n):
    if n<=0: return 
    for i in range(1,n):
        print(i, end=" ")
    print(n, end=" ")
    for i in range(n-1,0,-1):
        print(i, end=" ")


def countdown_recursion(e):
    if e<1: return
    cd_helper(1,e)
    

def cd_helper(c,e):
    if c==e: print(e, end=" ")
    else:
        print(c,end=" ")
        print(cd_helper(c+1,e), end=" ")
    return c-1

def super_jagged(l:list):
    out=[]
    if len(l)==0 or len(l)==1: return l 
    copy=l
    nl=copy.pop(0)
    out+= [[l[0]]+ super_jagged([nl])]

    print(out)


def main():
    # print(factorial(7))
    # countdown_recursion(5)
    super_jagged([1,2,3,4,5,6,7])




if __name__=="__main__":
    main()