
## CS131 Assignment 7
## Prajwal Bhandari
## Feb 2024


## Helper Function:
def inlist(x,l):
    for i in range(len(l)):
        if l[i]==x:
            return True
    return False


def frequency_analysis(s):
    chars=[]
    nums=[]
    outl=[chars,nums]
    for i in range(len(s)):
        if s[i] not in chars:
            chars+=[s[i]]
            nums+=[1]
        else: 
          for j in range(len(chars)):
            if chars[j]==s[i]:          
                nums[j]+=1    
    print(outl)          
    return outl


def bubble_sort(l):
    temp=0
    for j in range(len(l)+1):
        for i in range(len(l)-j-1):
            if l[i]>l[i+1]:
                temp=l[i+1]
                l[i+1]=l[i]
                l[i]=temp
    print(l)
    return l


def shaker_sort(l):
    temp=0
    for j in range(len(l)+1):
        for i in range(j,len(l)-j-1):
            if l[i]>l[i+1]:
                temp=l[i+1]
                l[i+1]=l[i]
                l[i]=temp
        for i in range(len(l)-j-1,j,-1):
            if l[i]<l[i-1]:
                temp=l[i-1]
                l[i-1]=l[i]
                l[i]=temp
    print(l)
    return l


def sorted_frequencies(s):
    chars=[]
    nums=[]
    outl=[chars,nums]
    for i in range(len(s)):
        if inlist(s[i],chars)==False:
            chars+=[s[i]]
            nums+=[1]
        else: 
          for j in range(len(chars)):
            if chars[j]==s[i]:          
                nums[j]+=1              
    
    temp=0
    temp2=0
    for j in range(len(nums)+1):
        for i in range(len(nums)-j-1):
            if nums[i]>nums[i+1]:
                temp=nums[i+1]
                nums[i+1]=nums[i]
                nums[i]=temp

                temp2=chars[i+1]
                chars[i+1]=chars[i]
                chars[i]=temp2

    print(outl)
    return outl
       

def main():
    # frequency_analysis("good morning America!")
    # bubble_sort([])
    shaker_sort([6,5,4,3,2,1])
    sorted_frequencies("Goooooooooood morning Penn State!!")
if __name__=="__main__":
    main()