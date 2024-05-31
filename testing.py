
def multi_print(num,str):
    if len(str)<len(num):
        minLen=len(str)
    else: 
        minLen=len(num)
    for i in range(minLen):
        for j in range(num[i]):
            print(str[i])

def universal_convert(chars,temps):
    if len(chars)<len(temps):                  #c>f c*1.8 + 32  f>c (f-32)/1.8
        minlen=len(chars)
    else:
        minlen=len(temps)
    outlist=[]
    for i in range(minlen):
        if chars[i]=="c":
            tempf=temps[i]*1.8 + 32
            outlist+=[tempf]
        elif chars[i]=="f": 
            tempc=(temps[i]-32)/1.8
            outlist+=[tempc]
        else: 
            outlist+=[temps[i]]
            pass
    print(outlist)


def drop_lowest(lst):
    if lst==[]:
        return
    lowestValue=lst[0]
    outl=[]
    LowestValueIndex=0
    for i in range(len(lst)):
        if lst[i]<lowestValue:
            lowestValue=lst[i]
            LowestValueIndex=i

    for i in range(len(lst)):
        if i==LowestValueIndex:
            pass
        else: outl+=[lst[i]]
    print(outl)


def points_to_percents(name, names, earned, listed):
    """Converts the points `got` and points `max` lists into a list percentages
    for the names matching `name`.

    All lists should be the same length.

    Args:
        name (str): The assignment name to convert.
        names (list[str]): A list of assignment names.
        earned (list[float]): A list of points earned.
        listed (list[float]): A list of points listed on the assignment.

    Returns:
        A list of percentages for the requested assignment name.
    """
    scores=[]
    if len(names)==len(earned) and len(earned)==len(listed):
        for i in range(len(names)):
            if names[i]==name:
                scores+=[(earned[i]/listed[i])*100]
            else:pass
        print(scores)
        return scores
    else: 
        print("Lists must all be the same length!")

    # TODO; Write this function


def unweighted_score(scores: list[float], length: int):
    """Calculate the unweighted score from a list of percentages.

    If `len(scores)` is greater than `length`, drop as many as is needed to only
    ever have at most `length` .

    Args:
        scores (list[float]): A list of scores.
        length (int): The maximum number of entries to use.

    Returns:
        The average score.
    """
    for i in range(len(scores)):
        if scores[i]<=0:
            print("Invalid Score!")
            return
    
    # Drop all lowest values that we can
    while len(scores) > length:
        # scores = drop_lowest(scores)

        total=0
    for i in range(len(scores)):
        total+=scores[i]
    total/=len(scores)

    return total 


def round_one(value):
    value*=10
    value+=0.5
    value-= value%1.0
    value/=10
    return value  # TODO; Write this function


def lists():
    l=[[1,2,3],[4,5,6],[7,8,9]]
    print(l[2][2]) #need to put the row first, then column **MUST BE ZERO INDEXED** 


def min_of_all(l):
    outl=[]
    # minlen=len(l[0])
    # for i in range(len(l)):
    #     if len(l[i])!=minlen or len(l[i])==0:
    #         print("Lists must all be uniform length and cannot be empty!")
    #         return 
    
    for i in range(len(l)):
        minvalue=l[i][0]
        for j in range(len(l[i])):
            if l[i][j]<minvalue:
                minvalue=l[i][j]
        outl+=[minvalue]

    print(outl)


def matrix_print(l):
    # minlen=len(l[0])
    # for i in range(len(l)):
    #     if len(l[i])!=minlen or len(l[i])==0:
    #         print("Lists must all be uniform length and cannot be empty!")
    #         return 

    #TODO:implement a feature where if the entries in the list are less than the max length, we fill the spots with 0s

    print(" [")
    for i in range(len(l)):
        for j in range(len(l[i])):
            if len(l[i])==0:
                pass
            else:
                print('  ',l[i][j], end="\t")
        print()
    print(" ]")


ALL_CHARS="aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ"

def numofchars(s: str):
    outl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

    for j in range(len(ALL_CHARS)):
        for i in range(len(s)):
            if s[i]==ALL_CHARS[j]:
                outl[j//2]+=1
            else: 
                pass
    print(outl)

def tracker(string):
    dic = {}
    for char in string:
        if char in dic:
            dic[char] +=1
        else:
            dic[char] = 1
        
def num_of_single_letter(s,c):
    total=0
    for i in range(len(s)):
        if s[i]==c:
            total+=1
    print(total)


def find(tof,s): ##tof: string to find, s: larger string
    if len(tof)>len(s):
        print("Invalid, string must be of less or equal length!")
        return
    if tof=="":
        print("Impossible to find an empty string!")
        return False
    
    j=0
    for i in range(len(s)):
        if s[i]==tof[j]:
            j+=1
            if j>=len(tof):
                print("Find: True")
                return True
        else:
            j=0
    print("Find: False")
    return False


def palindrome(x):
    for i in range(len(x)//2):
        if x[i]!=x[len(x)-i-1]:
           print("False")
           return
    print("True")


def all_sum(l):
    if len(l)==0:
        return []
    else:
        return ash(l,0)

def ash(l,i):
    if i==len(l)-1:
        return [l[i]]
    
    value= ash(l, i+1)
    return [l[i]+value[0]]+value 




def main():
    print(all_sum([1,2,3,4,5,6]))

if __name__== "__main__":
    main()