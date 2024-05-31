
def fib(n:int) ->int: 
    if n<1: return 0 
    if n==1: return 1
    if n==2: return 2 

    return fib(n-1)+fib(n-2)


def fib_memo(n:int):
    if n<1: 
        return 0 
    else:
        return _fib_memo(n,{0:0, 1:1})


def _fib_memo(n:int,d: dict[int,int]) ->int:
    if d.get(n,-1)!= -1:
        return d.get(n,-1)
    else: 
       d[n]= _fib_memo(n-1,d) + _fib_memo(n-2,d)
       return d[n]
    
print(fib_memo(120))


    




