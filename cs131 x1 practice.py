
## CS131 Exam 1 Practice
## Prajwal Bhandari
## Feb 2024

def absolute(x):
    if x<=0:
        print(-x)
    else: 
        print(x)


def manual_multiply(num,mult):
    total=0
    if mult<0:
        for i in range(0,mult-1,-1):
            total-=num
    else:
        for i in range(mult+1):
            total+=num
    print(total)


def xy_mangitude(x1,y1,x2,y2):
    print(((x2-x1)**2+(y2-y1)**2)**(1/2))
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)


def print_point(x,y,):
    print("(", x, ",", y, ")",sep="")


def position_vector(x1,y1,x2,y2):
    x=(x2-x1)
    y=(y2-y1)
    print_point(x,y)


def xy_normal(x1,y1,x2,y2):
    pass


def main():
    absolute(-10)
    manual_multiply(-13,-21)
    xy_mangitude(1,2,4,6)
    print_point(3,4)
    position_vector(1,2,3,4)
if __name__=="__main__":
    main()