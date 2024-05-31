
## CS131 Assignment/Exerccise 8
## Prajwal Bhandari
## March 2024


SUITS=["C","D","H","S"]
CARDS=["1", "2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def isin(a,b:list)->bool:
    for i in range(len(b)):
        if b[i]==a:
            return True
    return False

def values(s:str) ->int:
    if s[1]=="1":
        val=1
    elif s[1]=="2":
        val=2
    elif s[1]=="3":
        val=3
    elif s[1]=="4":
        val=4
    elif s[1]=="5":
        val=5
    elif s[1]=="6":
        val=6
    elif s[1]=="7":
        val=7
    elif s[1]=="8":
        val=8
    elif s[1]=="9":
        val=9
    elif s[1]=="T": 
        val=10
    elif s[1]=="J":
        val=10
    elif s[1]=="Q":
        val=10
    elif s[1]=="K":
        val=10
    elif s[1]=="A":
        val=11
    else: 
        return "invalid input!"
    return val

def isace(s:str)-> bool:
    if s[1]=="A" or s[1]=="1":
        return True
    return False

############ there is a problem with list heirarchy. fix later ############

def blackjack_checker(cards:list[str]) ->list[list[str]]:
    temp=[]
    total=0
    hands=[]
    seen=[]
    duplicate=[]
    ace_suits=[]
    
    ## Preliminary check: 
    if cards==[]: 
        return [hands,duplicate]
    for i in range(len(cards)):
        if  not (isin(cards[i][0],SUITS) and isin(cards[i][1],CARDS)) or len(cards[i])!=2:
            print("card",i+1, "is invalid!")
            return []
    for j in range(len(cards)):
        #check if card is a duplicate ace, and track what aces we have seem
        if isace(cards[j]) and not isin(cards[j][0],ace_suits):
            ace_suits += [cards[j][0]]
        elif isace(cards[j]) and isin(cards[j][0],ace_suits) and not isin(cards[j],duplicate):
            duplicate += [cards[j]]

        #putting the cards into our output list 
        if total+values(cards[j])<=21:
            total+=values(cards[j])
            temp+=[cards[j]]
        else:
            hands+=[temp]
            temp=[cards[j]]
            total=values(cards[j])
        #check for duplicate cards (that arent aces since we already programmed in what we will do for aces)
        if isin(cards[j],seen) and not isin(cards[j],duplicate):
            duplicate+=[cards[j]]

        seen+=[cards[j]]

    hands+=[temp]


    return [hands,duplicate]

def main():
    print(blackjack_checker([]))
    print(blackjack_checker(["HK", "S6", "D9", "D8", "S1", "S1", "S1", "H2", "C2", "C2", "C2"]))
if __name__=="__main__":
    main()


            

    